# Backend API

A modern FastAPI backend for the Attendance Management System with PostgreSQL database and JWT authentication.

## Features

- 🚀 **FastAPI**: High-performance async API framework
- 🔐 **JWT Authentication**: Secure token-based authentication
- 🗄️ **PostgreSQL**: Robust relational database
- 📊 **SQLAlchemy**: Modern Python SQL toolkit and ORM
- 🔄 **Database Migrations**: Alembic for schema management
- 📝 **API Documentation**: Auto-generated OpenAPI/Swagger docs
- ✅ **Data Validation**: Pydantic models for request/response validation
- 🧪 **Testing**: Pytest with test database setup

## Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL** - Advanced open-source relational database
- **SQLAlchemy** - Python SQL toolkit and ORM
- **Alembic** - Database migration tool
- **Pydantic** - Data validation using Python type annotations
- **JWT** - JSON Web Tokens for authentication
- **Uvicorn** - ASGI server for production deployment

## Setup Guide

### Prerequisites

- Python 3.11+ installed
- PostgreSQL 14+ installed and running
- pip or poetry package manager

### Installation

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or if using Poetry:
   ```bash
   poetry install
   ```

4. **Set up environment variables:**
   Create a `.env` file in the backend directory:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/attendance_db
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Set up the database:**
   ```bash
   # Create database (if not exists)
   createdb attendance_db
   
   # Run migrations
   alembic upgrade head
   ```

6. **Start the development server:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Available Scripts

- `uvicorn app.main:app --reload` - Start development server
- `alembic revision --autogenerate -m "message"` - Create new migration
- `alembic upgrade head` - Apply migrations
- `pytest` - Run tests
- `pytest --cov=app` - Run tests with coverage

### Project Structure

```
app/
├── api/
│   ├── auth.py          # Authentication endpoints
│   ├── users.py         # User management endpoints
│   └── attendance.py    # Attendance endpoints
├── core/
│   ├── config.py        # Configuration settings
│   ├── security.py      # JWT and password utilities
│   └── database.py      # Database connection
├── db/
│   ├── models.py        # SQLAlchemy models
│   └── schemas.py       # Pydantic schemas
├── main.py              # FastAPI application
└── dependencies.py      # Dependency injection
```

### API Endpoints

#### Authentication
- `POST /auth/login` - User login
- `POST /auth/register` - User registration
- `POST /auth/refresh` - Refresh access token

#### Users
- `GET /users/me` - Get current user profile
- `PUT /users/me` - Update user profile
- `GET /users/` - List users (admin only)

#### Attendance
- `POST /attendance/checkin` - Check in attendance
- `POST /attendance/checkout` - Check out attendance
- `GET /attendance/history` - Get attendance history
- `GET /attendance/report` - Generate attendance report

### Database Schema

#### Users Table
- `id` - Primary key
- `email` - Unique email address
- `username` - Unique username
- `hashed_password` - Encrypted password
- `role` - User role (student/teacher/admin)
- `created_at` - Registration timestamp

#### Attendance Table
- `id` - Primary key
- `user_id` - Foreign key to users
- `checkin_time` - Check-in timestamp
- `checkout_time` - Check-out timestamp (nullable)
- `location` - GPS coordinates (optional)
- `status` - Attendance status

### Development

#### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py
```

#### Database Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

#### API Documentation
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

### Production Deployment

1. **Set production environment variables:**
   ```env
   DATABASE_URL=postgresql://user:pass@prod-db:5432/attendance_db
   SECRET_KEY=secure-production-key
   DEBUG=False
   ```

2. **Run with production server:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

3. **Use Docker (optional):**
   ```bash
   docker build -t attendance-backend .
   docker run -p 8000:8000 attendance-backend
   ```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `SECRET_KEY` | JWT signing key | Required |
| `ALGORITHM` | JWT algorithm | HS256 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry time | 30 |
| `DEBUG` | Enable debug mode | False |

### Troubleshooting

- **Database connection issues**: Check PostgreSQL is running and credentials are correct
- **Migration errors**: Ensure database exists and user has proper permissions
- **Import errors**: Verify virtual environment is activated and dependencies installed
- **Port conflicts**: Change port with `--port` flag if 8000 is in use