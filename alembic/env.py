import os
import sys
from pathlib import Path
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine, pool, text
import pgvector.sqlalchemy  # noqa: F401

# Make app importable
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.db.base import Base  # noqa: E402
import app.db.models

# Alembic config
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Load DB URL
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

# Metadata
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    engine = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with engine.connect() as connection:
        # Enable pgvector (safe to run multiple times)
        connection.execute(text('CREATE EXTENSION IF NOT EXISTS "vector";'))

        # Optional debug (dev only)
        if os.getenv("DEBUG_ALEMBIC") == "1":
            result = connection.execute(
                text("SELECT current_database(), inet_server_addr(), inet_server_port();")
            )
            print("ALEMBIC CONNECTED TO:", result.fetchone())

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
