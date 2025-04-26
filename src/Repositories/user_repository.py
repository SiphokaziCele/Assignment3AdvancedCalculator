from Repositories.repository_interface import Repository
from Models.User import User

class UserRepository(Repository[User, str]):
    pass
