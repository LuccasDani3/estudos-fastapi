from schemas.user import UserCreate

users = []

class UserService:
    def create(self, user: UserCreate):
        users.append(user.model_dump())
        return user
    
def get_user_service():
    return UserService()