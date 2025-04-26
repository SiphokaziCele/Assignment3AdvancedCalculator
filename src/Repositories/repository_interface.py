from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')  # Entity type
ID = TypeVar('ID')  # ID type

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def save(self, entity: T) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        pass
