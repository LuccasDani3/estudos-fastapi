from fastapi import APIRouter

from schemas.user import UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Usuários"]
)

users = []

@router.post('/')
def create_user(user: UserCreate):
    users.append(user)
    return user