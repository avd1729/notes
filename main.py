from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from core import db
from models import user

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
    user_instance = user.User(username=username, email=email)
    db.add(user_instance)

    db.commit()
    db.refresh(user_instance)
    return {
        "name": username,
        "email": email
    }
