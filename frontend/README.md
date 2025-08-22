# Unified Property‑Search & Scheduling Portal

Modern buyers expect to search for properties and schedule viewings at any time without waiting on an agent.  This project implements a responsive web application for a real estate agency that allows clients to browse listings, filter by key criteria, and book appointments directly through the platform.  By automating these workflows, agents can focus on nurturing relationships while clients enjoy a smoother experience.

## Features

- **Property Search:** Query listings by location, price range, number of bedrooms, and property type.  The backend exposes a RESTful API for fetching data from a database or an external MLS (Multiple Listing Service) source.
- **Responsive UI:** A mobile‑first front‑end built with HTML/CSS and vanilla JavaScript (or any framework of your choice) so the application looks great on phones, tablets, and desktops.
- **Scheduling:** Clients can select an available time slot and automatically book a viewing.  Agents receive notifications and the system sends confirmations and reminders.
- **Analytics:** Basic tracking of search patterns and scheduled viewings to inform marketing campaigns and operational decisions.
- **Extensible Architecture:** Separate front‑end and back‑end folders allow you to replace or enhance either layer without disrupting the other.

## Technology

This repository is organised into two main parts:

| Component | Technology | Description |
|----------|------------|-------------|
| **Backend** | [Flask](https://flask.palletsprojects.com/), Python | Exposes API endpoints for property search, scheduling, and analytics.  Can be configured to use SQLite, PostgreSQL, or to fetch data from an external MLS API. |
| **Frontend** | HTML/CSS/JavaScript | Implements the user interface for searching listings and booking appointments.  You can swap this out for React, Vue, or another framework if preferred. |
| **Data** | SQLite (default) | A simple relational database for storing property details, user accounts, and appointments.  Abstracted so you can migrate to another DBMS later. |

## Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/) installed on your machine.
- A modern web browser.
- (Optional) A virtual environment tool such as `venv` or `conda`.

### Installation

1. **Clone the repository** (or copy these files into a new GitHub project):
   ```bash
   git clone https://github.com/mraddai/improvedUnifiedREportal
   cd real_estate_portal
   ```

2. **Set up the backend:**
   ```bash
   cd backend
   python3 -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   python app.py
   ```
   By default, the Flask server will run at `http://localhost:5000/`.

3. **Open the frontend:** In a separate terminal, start a simple HTTP server in the `frontend` folder:
   ```bash
   cd ../frontend
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000/` in your browser.

### Environment Configuration

The backend reads its configuration from environment variables.  You can copy `backend/.env.example` to `.env` and modify it to point to your database or MLS API.

## Directory Structure

```
real_estate_portal/
├── backend/            # Python Flask API
│   ├── app.py          # Main application entry point
│   ├── database.db     # SQLite database (created at runtime)
│   ├── models.py       # SQLAlchemy models (not yet implemented)
│   └── requirements.txt# Backend Python dependencies
├── frontend/           # Client‑side code
│   ├── index.html      # Main HTML file
│   ├── style.css       # Stylesheet for layout and design
│   └── script.js       # Client‑side JavaScript
└── README.md           # Project overview (this file)
```

## Contributing

Contributions are welcome!  If you'd like to add new features or fix issues, please follow these steps:

1. Fork this repository and create a new branch for your feature or bug fix.
2. Write clear, concise commit messages and document any significant architectural decisions.
3. If you add dependencies or configuration, update the documentation accordingly.
4. Submit a pull request describing your changes and why they improve the project.

## License

This project is released under the MIT License.  See `LICENSE` for details.
