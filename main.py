from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from core import db
from models import user
from repositories.user_repository import UserRepository
from services.user_service import UserService

user.Base.metadata.create_all(bind = db.engine)

app = FastAPI()

def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


@app.post("/users/")
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    user_instance = user_service.create_user(username, email)
    return {
        "name": user_instance.username,
        "email": user_instance.email
    }
