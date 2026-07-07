from fastapi import APIRouter, Depends

from schemas.user import UserCreate
from services.user_service import UserService, get_user_service


router = APIRouter(
    prefix="/users",
    tags=["Usuários"]
)


@router.post('/')
def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service)
    ):
    
    return service.create(user)