from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate
from app.models import User  # if you have one
from app.database import db  # adjust as needed

router = APIRouter()

@router.post("/")
async def create_user(user: UserCreate):
    # Stubbed logic; you can replace with real database check
    if user.username == "dupeuser":
        raise HTTPException(status_code=400, detail="User already exists")
    return {"username": user.username, "email": user.email}

