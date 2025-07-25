from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserRead
from app.database import get_db
from app.models import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", response_model=list[UserRead])
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
