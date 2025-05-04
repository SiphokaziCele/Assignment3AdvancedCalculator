from src.Repositories.user_repository import UserRepository
from src.Models.User import User
from typing import Optional
import json
import os

class FileSystemUserRepository(UserRepository):
    def __init__(self, file_path="users.json"):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump({}, f)

    def save(self, user: User) -> None:
        data = self._read_data()
        data[user.user_id] = {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "password": user.password
        }
        self._write_data(data)

    def find_by_id(self, user_id: str) -> Optional[User]:
        data = self._read_data()
        if user_id in data:
            user_data = data[user_id]
            return User(**user_data)
        return None

    def find_all(self):
        data = self._read_data()
        return [User(**info) for info in data.values()]

    def delete(self, user_id: str) -> None:
        data = self._read_data()
        if user_id in data:
            del data[user_id]
            self._write_data(data)

    def _read_data(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _write_data(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)
