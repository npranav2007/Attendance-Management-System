from __future__ import annotations


from contextlib import contextmanager
from typing import Generator, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import POSTGRESQL_CONNECTION_STRING



# Load .env (if present) so environment variables are available



def _get_database_url() -> str:
    """Resolve a PostgreSQL connection URL from common environment variables.

    Checks `POSTGRESQL_CONNECTION_STRING` then `DATABASE_URL`. Raises RuntimeError
    when neither is set.
    """
    url = POSTGRESQL_CONNECTION_STRING
    if not url:
        raise RuntimeError(
            "Database connection string not found. Set POSTGRESQL_CONNECTION_STRING or DATABASE_URL in environment."
        )
    return url


# SQLAlchemy engine and session factory (module-level singletons)
DATABASE_URL: str = _get_database_url()

# create_engine accepts a URL string; for psycopg2-binary the URL should start with postgresql://
engine = create_engine(DATABASE_URL, future=True)
SessionLocal: sessionmaker = sessionmaker(bind=engine, autoflush=False, autocommit=False, class_=Session)


# Declarative base for models to inherit
Base = declarative_base()


def get_engine():
    """Return the SQLAlchemy engine instance."""
    return engine


def get_session() -> sessionmaker:
    """Return the sessionmaker factory."""
    return SessionLocal


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Yield a database session and ensure it is closed.

    Use as a dependency in FastAPI routes or as a context manager in scripts:

        with get_db() as db:
            ...
    """
    db: Optional[Session] = None
    try:
        db = SessionLocal()
        yield db
        db.commit()
    except SQLAlchemyError:
        if db is not None:
            db.rollback()
        raise
    finally:
        if db is not None:
            db.close()


def init_db(drop_all: bool = False) -> None:
    """Create (and optionally drop) database tables for all imported models.

    Important: import your models module(s) before calling this so model classes are
    registered on `Base.metadata`.
    """
    if drop_all:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


__all__ = ["engine", "SessionLocal", "Base", "get_db", "init_db", "get_engine", "get_session"]
