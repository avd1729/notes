from sqlalchemy.orm import Session
from sqlalchemy.future import select
from models import user

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str):
        user_instance = user.User(username=username, email=email)
        self.db.add(user_instance)
        self.db.commit()
        self.db.refresh(user_instance)
        return user_instance
    
    def get_all_users(self):
        result = self.db.execute(select(user.User))
        return result.scalars().all()