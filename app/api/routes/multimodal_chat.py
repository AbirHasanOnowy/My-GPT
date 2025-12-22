from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.conversation_log import ConversationLog
from app.schemas.chat import ChatLogCreate, ChatLogOut
from app.api.routes.auth import get_current_user
from app.db.models.user import User

router = APIRouter()

@router.post("/", response_model=ChatLogOut)
def create_chat_log(
    payload: ChatLogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    log = ConversationLog(
        user_id=current_user.id,
        text_query=payload.text_query,
        response_text="(placeholder response)"
    )

    db.add(log)
    db.commit()
    db.refresh(log)
    return log

@router.get("/history", response_model=list[ChatLogOut])
def get_chat_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(ConversationLog)
        .filter(ConversationLog.user_id == current_user.id)
        .order_by(ConversationLog.timestamp.desc())
        .all()
    )
