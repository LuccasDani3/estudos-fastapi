from fastapi import Depends

from schemas.user import UserCreate
from repositories.user_repository import UserRepository, get_user_repository

class UserService:
    def create(
            self,
            user: UserCreate,
            service: UserRepository = Depends(get_user_repository)
        ):
        return service.create()
    
def get_user_service():
    return UserService()