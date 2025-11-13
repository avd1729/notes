from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from core import db

app = FastAPI()

def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()