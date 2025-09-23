from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import POSTGRESQL_CONNECTION_STRING


# Create engine and session factory
engine = create_engine(POSTGRESQL_CONNECTION_STRING, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Provide a transactional database session."""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise
    finally:
        db.close()


def init_db(drop_all: bool = False) -> None:
    """Initialize database schema (optionally dropping existing tables)."""
    if drop_all:
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
