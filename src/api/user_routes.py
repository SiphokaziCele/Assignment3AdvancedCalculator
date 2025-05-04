from fastapi import APIRouter, HTTPException
from src.Models.User import UserResponse
from src.services.user_service import UserService
from src.RepositoryFactory.repository_factory import RepositoryFactory

router = APIRouter(prefix="/api/users", tags=["Users"])
user_service = UserService(RepositoryFactory.get_user_repository("FILE"))

@router.post("/", response_model=UserResponse)
def create_user(user: UserResponse):
    try:
        return user_service.register_user(user.user_id, user.name, user.email, user.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    try:
        return user_service.get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
