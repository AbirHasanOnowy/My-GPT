from typing import ClassVar
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str           # Will be read from .env
    SECRET_KEY: str             # Will be read from .env
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60  # Default value if not in .env
    UPLOAD_DIR: ClassVar[str] = "app/uploads"

    class Config:
        env_file = ".env"       # Load environment variables from this file
        env_file_encoding = "utf-8"

# Instantiate settings
settings = Settings()
