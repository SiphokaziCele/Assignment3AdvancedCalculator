# src/Models/User/user.py

from src.Models.History import History
from pydantic import BaseModel

# Business Logic Class (NOT used as response model)
class User:
    def __init__(self, userID: int, name: str, email: str, password: str):
        self.user_id = userID
        self.name = name
        self.email = email
        self.password = password
        self.history = History(userID)

    def register(self):
        print(f"{self.name} registered successfully.")

    def login(self):
        print(f"{self.name} logged in.")

    def logout(self):
        print(f"{self.name} logged out.")

    def add(self):
        print("booyakasha.")

# ✅ Pydantic model used in response_model=
class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str

    class Config:
        from_attributes = True  # ✅ Pydantic v2 replacement for orm_mode
