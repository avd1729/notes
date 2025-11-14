from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username: str, email: str, password: str):
        return self.user_repository.create_user(username, email, password)
    
    def get_all_users(self):
        return self.user_repository.get_all_users()