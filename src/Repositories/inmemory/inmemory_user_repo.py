from Repositories.user_repository import UserRepository
from Models.User import User
from typing import Optional

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._storage = {}

    def save(self, user: User) -> None:
        self._storage[user.user_id] = user

    def find_by_id(self, user_id: str) -> Optional[User]:
        return self._storage.get(user_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, user_id: str) -> None:
        if user_id in self._storage:
            del self._storage[user_id]
