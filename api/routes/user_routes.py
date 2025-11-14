from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.db import get_db
from services.user_service import UserService
from repositories.user_repository import UserRepository

router = APIRouter(prefix="/users")

@router.post("/")
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    user_instance = user_service.create_user(username, email)
    return {
        "name": user_instance.username,
        "email": user_instance.email
    }

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    result = user_service.get_all_users()
    return {
        "result": result
    }