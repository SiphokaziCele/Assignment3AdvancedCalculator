from src.Repositories.repository_interface import Repository
from src.Models.User import User

class UserRepository(Repository[User, str]):
    pass
