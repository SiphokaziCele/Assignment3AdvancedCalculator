import unittest
from services.user_service import UserService
from Repositories.inmemory.inmemory_user_repo import InMemoryUserRepository

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryUserRepository()
        self.service = UserService(self.repo)

    def test_register_and_get_user(self):
        user = self.service.register_user("U1", "Test", "test@example.com", "pass")
        self.assertEqual(user.name, "Test")
        retrieved = self.service.get_user("U1")
        self.assertEqual(retrieved.email, "test@example.com")

    def test_duplicate_user(self):
        self.service.register_user("U1", "Test", "test@example.com", "pass")
        with self.assertRaises(ValueError):
            self.service.register_user("U1", "Test", "test@example.com", "pass")
