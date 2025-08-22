"""
Main Flask application for the unified property‑search and scheduling portal.

This module exposes two example endpoints:

* `GET /properties` returns a list of property objects.  In a real
  application, this would query a database or external MLS API.  The
  response structure includes basic fields like id, address, price and
  features.

* `POST /schedule` accepts JSON with a property id, client contact
  information and a desired appointment time.  The example
  implementation simply echoes the request.  In production, you would
  validate input, persist to a database and notify the responsible
  agent.

Environment variables (loaded from a `.env` file when available) are
used to configure the application.  See `backend/.env.example` for
default values.
"""

from __future__ import annotations

import os
from datetime import datetime
from typing import Any, Dict, List

from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env if present

app = Flask(__name__)

# Example in‑memory data.  Replace with a proper database or
# integration with a Multiple Listing Service (MLS) API in production.
PROPERTIES: List[Dict[str, Any]] = [
    {
        "id": 1,
        "address": "123 Main St",
        "city": "Metropolis",
        "price": 350_000,
        "bedrooms": 3,
        "bathrooms": 2,
        "amenities": ["garage", "garden"],
    },
    {
        "id": 2,
        "address": "456 Elm Ave",
        "city": "Smallville",
        "price": 275_000,
        "bedrooms": 2,
        "bathrooms": 1.5,
        "amenities": ["pool", "fireplace"],
    },
]


@app.route("/properties", methods=["GET"])
def get_properties() -> Any:
    """Return a JSON list of property data.

    In a real application you would accept query parameters for
    filtering (e.g. price range, city, number of bedrooms) and use
    them to filter the results from a database.
    """
    return jsonify(PROPERTIES)


@app.route("/schedule", methods=["POST"])
def schedule_viewing() -> Any:
    """Schedule a viewing for a property.

    Expected JSON body:
    ```json
    {
        "property_id": 1,
        "client_name": "John Doe",
        "client_email": "john@example.com",
        "preferred_time": "2025-08-23T14:00:00"
    }
    ```

    The current implementation validates the input and returns a
    confirmation.  Integrate with a database and email/calendar
    service for a production implementation.
    """
    data = request.get_json(force=True) or {}
    required_fields = ["property_id", "client_name", "client_email", "preferred_time"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Validate date/time format
    try:
        preferred_time = datetime.fromisoformat(data["preferred_time"])
    except ValueError:
        return jsonify({"error": "preferred_time must be ISO 8601 format"}), 400

    # In a production system you'd save this to the database and notify the agent
    response = {
        "message": "Viewing scheduled successfully",
        "property_id": data["property_id"],
        "scheduled_for": preferred_time.isoformat(),
        "client": {
            "name": data["client_name"],
            "email": data["client_email"],
        },
    }
    return jsonify(response), 201


if __name__ == "__main__":
    app.run(debug=True)