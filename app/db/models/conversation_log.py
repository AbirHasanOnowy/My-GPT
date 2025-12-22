import uuid
from sqlalchemy import Column, Text, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector

from app.db.base import Base

EMBEDDING_DIM = 768  # BLIP-2 typical size (can change later)

class ConversationLog(Base):
    __tablename__ = "conversation_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    text_query = Column(Text, nullable=True)

    # Stage 7+
    image_urls = Column(JSONB, nullable=True)
    vlm_output = Column(JSONB, nullable=True)

    response_text = Column(Text, nullable=False)

    # Stage 7+ (must be nullable for now)
    llm_model_name = Column(Text, nullable=True)
    vlm_model_name = Column(Text, nullable=True)

    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", backref="conversation_logs")

    __table_args__ = (
        Index("ix_conversation_user_id", "user_id"),
    )
