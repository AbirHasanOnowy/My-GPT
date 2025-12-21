from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from uuid import UUID
from typing import Optional

from app.db.session import get_db
from app.db.models.user import User
from app.core.security import hash_password, verify_password, create_access_token, decode_access_token
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse, UserResponse

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# -------------------------
# Register endpoint
# -------------------------
@router.post("/register", response_model=UserResponse)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    print("Password before hashing:", request.password)

    
    new_user = User(
        email=request.email,
        password_hash=hash_password(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return UserResponse(
        id=new_user.id,
        email=new_user.email,
        created_at=new_user.created_at,
        updated_at=new_user.updated_at
    )


# -------------------------
# Login endpoint
# -------------------------
@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token({"sub": str(user.id)})
    return TokenResponse(access_token=access_token)


# -------------------------
# Dependency: get current user
# -------------------------
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user_id_str: Optional[str] = payload.get("sub")
    if not user_id_str:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
    
    try:
        user_id = UUID(user_id_str)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user ID in token")
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user


# -------------------------
# Example protected route
# -------------------------
@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        created_at=current_user.created_at,
        updated_at=current_user.updated_at
    )
