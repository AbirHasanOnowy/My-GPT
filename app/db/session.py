from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings  # or from pydantic_settings import Settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)  # echo=True for debugging
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency for FastAPI
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
