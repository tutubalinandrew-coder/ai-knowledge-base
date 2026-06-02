from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.core.database import get_db

router = APIRouter(prefix="/api")


@router.post("/users", response_model=UserRead)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        telegram_id=user_data.telegram_id,
        username=user_data.username
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users", response_model=list[UserRead])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return (users)