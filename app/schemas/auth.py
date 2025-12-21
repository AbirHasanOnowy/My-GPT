from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime


# -------------------------
# Request Schemas
# -------------------------
class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# -------------------------
# Response Schemas
# -------------------------
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    created_at: datetime
    updated_at: datetime
