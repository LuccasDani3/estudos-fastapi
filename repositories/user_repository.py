from schemas.user import UserCreate

users = []

class UserRepository:
    def create(
        self,
        user: UserCreate,
    ):
        users.append(user.model_dump())
        return user
    

    def list(self):
        return users
    

    def get_by_id(self, user_id: int):
        pass
    

    def update(self, user_id: int):
        pass
    
    
    def delete(self, user_id: int):
        pass
    

def get_user_repository():
    return UserRepository()