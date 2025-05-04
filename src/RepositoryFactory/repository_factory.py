from src.Repositories.json_repo.filesystem_user_repo import FileSystemUserRepository

class RepositoryFactory:
    @staticmethod
    def get_user_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            from Repositories.inmemory.inmemory_user_repo import InMemoryUserRepository
            return InMemoryUserRepository()
        elif storage_type == "FILE":
            return FileSystemUserRepository()
        else:
            raise ValueError("Invalid storage type")
