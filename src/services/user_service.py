from src.Repositories.user_repository import UserRepository
from src.Models.User import User

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register_user(self, user_id: str, name: str, email: str, password: str) -> User:
        if self.repo.find_by_id(user_id):
            raise ValueError("User already exists")
        user = User(user_id, name, email, password)
        self.repo.save(user)
        return user

    def get_user(self, user_id: str) -> User:
        user = self.repo.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user
