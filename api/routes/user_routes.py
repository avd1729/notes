from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.db import get_db
from services.user_service import UserService
from repositories.user_repository import UserRepository

router = APIRouter()

@router.post("/users/")
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    user_instance = user_service.create_user(username, email)
    return {
        "name": user_instance.username,
        "email": user_instance.email
    }