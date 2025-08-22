# Development Guidelines

This document provides high‑level guidance for implementing and expanding the unified property‑search and scheduling portal.  Follow these practices to keep the codebase maintainable and professional.

## Architectural Guidelines

1. **Separation of concerns:** Keep the front‑end (UI) and back‑end (API) in distinct folders (`frontend/` and `backend/`) so they can evolve independently.  Avoid coupling business logic to presentation code.
2. **API design:** Use RESTful conventions for endpoints (e.g. `/properties` for listing and `/schedule` for creating appointments).  Return clear status codes and JSON responses.  Document endpoints using OpenAPI or similar tooling as the project matures.
3. **Configuration:** Load secrets and environment‑specific settings from environment variables (see `backend/.env.example`).  Do not commit real credentials to version control.
4. **Database:** Start with SQLite for local development, but abstract data access through an ORM (e.g. SQLAlchemy) so it’s easy to switch to PostgreSQL or another database.  Model entities such as `Property`, `User`, and `Appointment` in `models.py`.
5. **Scheduling:** Integrate with a calendar service (e.g. Google Calendar or Outlook) for real booking flows.  Ensure that time slots are validated and don’t conflict with existing appointments.
6. **Security:** Implement input validation, CSRF protection and authentication.  Only authorized agents should be able to add or edit properties.
7. **Testing:** Write unit and integration tests for API endpoints.  Use tools like `pytest` and `Flask‑Testing` to simulate HTTP requests and assert expected behaviour.

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code and use a linter (e.g. `flake8`) to enforce consistency.
- Use descriptive variable names and docstrings to clarify the purpose of modules, classes and functions.
- Keep functions small; if a function grows too large, refactor it into smaller helpers.

## Git & Collaboration

1. Create a new branch for each feature or bug fix (`feature/search-filtering`, `bugfix/appointment-timezone` etc.).
2. Write meaningful commit messages that explain why a change was made.
3. Keep pull requests focused and concise.  Avoid bundling unrelated changes.
4. Review code for readability, performance and security before merging.

## Future Enhancements

Here are some ideas for expanding the project:

- **Advanced Filtering:** Add search by square footage, year built, or amenities.  Implement geospatial queries using a mapping service.
- **User Accounts:** Allow clients to register, save searches, and view their appointment history.
- **Real‑time Messaging:** Integrate chat or messaging between clients and agents to coordinate details.
- **Analytics Dashboard:** Build out the analytics component to visualize popular search terms, conversion rates, and agent performance.
- **Deployment:** Containerize the application with Docker and set up CI/CD for automated testing and deployment.

Following these guidelines will help ensure the project remains organised, scalable and easy to contribute to as it grows.