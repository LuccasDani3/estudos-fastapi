from schemas.user import UserCreate
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository):
        self.repository = repository


    def create(
            self,
            user: UserCreate,
        ):
        return self.repository.create(user)
    

    def list(self):
        return self.repository.list()
    

    def get_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)
    

    def update(self, user_id: int):
        return self.repository.update(user_id)
    
    
    def delete(self, user_id: int):
        return self.repository.delete(user_id)


def get_user_service():
    repository = UserRepository()
    service = UserService(repository)
    return service