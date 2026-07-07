from schemas.user import UserCreate

users = []

class UserRepository:
    def create(
        self,
        user: UserCreate,
    ):
        users.append(user.model_dump(user))
        return user
    
def get_user_repository():
    return UserRepository()