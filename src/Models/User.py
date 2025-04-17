# user.py
from History import History

class User:
    def __init__(self, userID, name, email, password):
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
        print(f"booyakasha.")
