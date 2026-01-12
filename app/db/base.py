from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# import all models here so Alembic sees them
from app.db.models.user import User
from app.db.models.conversation_log import ConversationLog
