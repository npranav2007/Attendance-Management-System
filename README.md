# Attendance Management System

This repository contains a cross-platform attendance management system with:

- `ams/` — React Native / Expo frontend
- `Backend/` — FastAPI backend using SQLAlchemy and PostgreSQL

This README covers local setup and common tasks for both frontend and backend on Windows (PowerShell) and Unix-like systems.

## Table of contents

- [Prerequisites](#prerequisites)
- [Backend setup (FastAPI)](#backend-setup-fastapi)
- [Frontend setup (Expo)](#frontend-setup-expo)
- [Environment variables](#environment-variables)
- [Development tips & common issues](#development-tips--common-issues)
- [Testing and CI](#testing-and-ci)
- [Next steps](#next-steps)


## Prerequisites

- Python 3.12+ (pyproject requires >=3.12)
- Node.js 18+ and `npm` or `yarn` for the Expo frontend
- Git
- A PostgreSQL database (local or hosted). The project expects a `POSTGRESQL_CONNECTION_STRING`/`DATABASE_URL` environment variable.

Optional but recommended:
- Use a virtual environment (venv, pipx, or pyenv)
- Install `poetry` if you prefer to manage Python dependencies with it (project includes `pyproject.toml`).


## Backend setup (FastAPI)

Open a PowerShell window in `Backend/` and follow these steps.

1. Create and activate a virtual environment

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
# On cmd.exe: .venv\Scripts\activate.bat
```

2. Upgrade `pip` and install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt 2>$null || python -m pip install poetry && poetry install
# If you rely on pyproject directly without poetry, install core dependencies:
python -m pip install fastapi[standard] psycopg2-binary sqlalchemy python-dotenv cryptography
```

Note: the project includes a `pyproject.toml` listing the required libraries. If you prefer `pip` only, create a `requirements.txt` from `pyproject.toml` or use `poetry`.

3. Environment variables

Create a `.env` file in `Backend/` (the project already contains an example `.env`). At minimum set:

```
POSTGRESQL_CONNECTION_STRING=postgresql://user:password@host:5432/dbname
JWT_SECRET_KEY=your-secret-key
```

If you're using a hosted provider (Neon, PlanetScale, AWS RDS), include any required SSL options in the URL (for example, `?sslmode=require`).

4. Initialize database (optional)

The backend contains a SQLAlchemy helper. To create tables run a small script or use Python REPL:

```powershell
# from project root
cd Backend
python -c "from app.db.postgresql.db import init_db; import app.models.models; init_db()"
```

Ensure your models import path is correct and that they inherit from `Base` exposed by the DB helper.

5. Run the server (development)

```powershell
# from Backend/
uvicorn app.app:app --reload --host 127.0.0.1 --port 8000
# Or use 'python -m uvicorn app.app:app --reload' if uvicorn is installed in the venv
```

Open `http://127.0.0.1:8000/docs` to view the interactive OpenAPI docs.


## Frontend setup (Expo)

The frontend is located in `ams/` and uses Expo.

1. Install dependencies

```powershell
cd ams
npm install
# or: yarn install
```

2. Start the Expo dev server

```powershell
npm run start
# or: npm run android / npm run ios / npm run web
```

Use the Expo Go app on your phone (scan QR) or an emulator.


## Environment variables

- Backend reads environment variables via `python-dotenv`. Place variables in `Backend/.env` for development.
- Important vars:
	- `POSTGRESQL_CONNECTION_STRING` or `DATABASE_URL` — SQLAlchemy database URL
	- `JWT_SECRET_KEY` — secret for signing JWTs
	- `JWT_EXP_SECONDS` — token expiry in seconds (optional)


## Development tips & common issues

- If your `.env` contains a value like `psql 'postgresql://...'` (i.e., wrapped for shell usage), remove the `psql ` wrapper and quotes — SQLAlchemy expects a plain URL string.
- On Windows PowerShell, remember to activate virtualenv with `.\.venv\Scripts\Activate.ps1`.
- If you encounter `psycopg2` build issues, use `psycopg2-binary` (already present in `pyproject.toml`).


## Testing and CI

There are no test files included yet. Recommended next steps:

- Add `pytest` and create small unit tests for the `app/security` helpers and DB layer.
- Add a GitHub Actions workflow to install dependencies, run linting and tests.


## Next steps and improvements

- Add FastAPI authentication routes (`/auth/token`, `/auth/register`) using the `app/security` helpers.
- Provide an `async` DB layer using SQLAlchemy `AsyncEngine` and `AsyncSession` if desired.
- Add integration tests and a `docker-compose.yml` for local Postgres for reproducible development.


If you'd like, I can:

- Add FastAPI auth endpoints and example usage in the frontend.
- Create a `requirements.txt` or a `poetry.lock` for easier installation.
- Add CI workflow and sample unit tests.

---

If you want any of the suggested follow-ups, pick one and I will implement it and update the README accordingly.

