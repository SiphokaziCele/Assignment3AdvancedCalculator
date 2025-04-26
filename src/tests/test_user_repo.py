import unittest
from Repositories.inmemory.inmemory_user_repo import InMemoryUserRepository
from Models.User import User

class TestInMemoryUserRepository(unittest.TestCase):
    def test_crud_operations(self):
        repo = InMemoryUserRepository()
        user = User("U001", "Siphokazi", "siphokazi@gmail.com", "1234")

        repo.save(user)
        self.assertEqual(repo.find_by_id("U001").name, "Siphokazi")

        all_users = repo.find_all()
        self.assertEqual(len(all_users), 1)

        repo.delete("U001")
        self.assertIsNone(repo.find_by_id("U001"))
