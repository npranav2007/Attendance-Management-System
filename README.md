# Attendance Management System

This repository contains three projects: the `Backend` (FastAPI/Python), `student-interface` (React Native + Expo), and `teacher-interface` (React + Vite).

This README provides steps to set up the development environment on Windows (PowerShell). Adjust commands if you're using a different shell or OS.

---

## Prerequisites

- Git
- Python 3.11 (the `Backend/pyproject.toml` targets this — use `pyenv` or an installer)
- Node.js (LTS recommended) and `npm` or `yarn`
- Expo CLI (for `student-interface`)

Installers / links:

- Git: https://git-scm.com/
- Python: https://www.python.org/downloads/
- Node.js: https://nodejs.org/
- Expo CLI: run `npm install -g expo-cli` (see below)

---

## 1) Backend (Python / FastAPI)

Path: `Backend/`

This project uses Poetry / the `pyproject.toml` to manage dependencies. If you don't use Poetry, you can create a virtual environment and install packages with `pip`.

Steps (PowerShell):

1. Open PowerShell and navigate to the backend folder:

```powershell
cd 'd:\Projects\Attendance-Management-System\Backend'
```

### Install `uv`

Direct install (recommended):

- **Windows (PowerShell):**
  ```powershell
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

- **Linux / macOS:**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

Or via pip:

```powershell
python -m pip install --user uv
# or to install into the current venv
pip install uv
```

### Install dependencies from `uv.lock`:

```powershell
# From Backend/ directory
# This will create or sync a virtual environment and install the exact pinned packages
uv sync
# Or to explicitly install into the active venv use:
uv install
```

If `uv` is not available or you prefer a more common workflow, use Poetry or `venv` as described below.

3. If you prefer `venv` + `pip` instead of Poetry:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # if a requirements.txt exists, otherwise use poetry to export
```

4. Create a `.env` file if required. See `Backend/README.md` (if present) or `Backend/app/core/config.py` for environment variables used by the app. Typical variables:

- `DATABASE_URL` — Postgres connection string
- `SECRET_KEY` — app secret/key for signing tokens

Example `.env` (PowerShell heredoc):

```powershell
@"
DATABASE_URL=postgresql://user:password@localhost:5432/attendance_db
SECRET_KEY=replace-with-your-secret
"@ | Out-File -FilePath .env -Encoding utf8
```

5. Run the application (example using `uvicorn`):

```powershell
# From Backend/ (activated venv or Poetry shell)
poetry run uvicorn app.app:app --reload --host 0.0.0.0 --port 8000
# or if using venv:
.# .\.venv\Scripts\Activate.ps1
python -m uvicorn app.app:app --reload --host 0.0.0.0 --port 8000
```

API should be available at `http://localhost:8000` and docs at `http://localhost:8000/docs` (if FastAPI default docs are enabled).

---

## 2) student-interface (Expo / React Native)

Path: `student-interface/`

This is an Expo-managed React Native app. You can run it in Expo Go on your device or in an emulator.

Steps (PowerShell):

1. Open PowerShell and navigate to the student-interface folder:

```powershell
cd 'd:\Projects\Attendance-Management-System\student-interface'
```

2. Install dependencies:

```powershell
npm install
# or
pnpm install
# or
yarn install
```

3. Install Expo CLI globally (if not installed):

```powershell
npm install -g expo-cli
```

4. Start the Expo dev server:

```powershell
npm start
# or
expo start
```

5. Follow the QR code with Expo Go on your phone or run an emulator via the Metro UI.

Note: If the app must connect to the backend running on your computer, ensure you use your machine's local IP (for phone testing) or `localhost`/`127.0.0.1` appropriately when using an emulator.

---

## 3) teacher-interface (React + Vite)

Path: `teacher-interface/`

This is a Vite React app. Steps (PowerShell):

1. Open PowerShell and navigate to the teacher-interface folder:

```powershell
cd 'd:\Projects\Attendance-Management-System\teacher-interface'
```

2. Install dependencies:

```powershell
npm install
# or
pnpm install
# or
yarn install
```

3. Start the dev server:

```powershell
npm run dev
# or
pnpm dev
# or
yarn dev
```

4. Open `http://localhost:5173` (or the address printed by Vite) to view the app.

---

## Common troubleshooting

- If a command like `python`, `npm`, or `poetry` is not found, add its install directory to your PATH or use the full path to the executable.
- For Python dependency issues, make sure the correct Python version is active. Use `python --version` to verify.
- If Postgres is required but not running, install Postgres and create the database referenced in `DATABASE_URL`.
- On Windows, PowerShell's execution policy can prevent activating virtual environments. Run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force` as admin if you run into script execution errors when activating venvs.

---

## Project structure (top-level)

- `Backend/` — Python FastAPI backend
- `student-interface/` — Expo React Native app for students
- `teacher-interface/` — Vite React app for teachers

---
