from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class ChatLogCreate(BaseModel):
    text_query: str | None = None

class ChatLogOut(BaseModel):
    id: UUID
    text_query: str | None
    response_text: str | None
    timestamp: datetime  

    class Config:
        from_attributes = True
