from domain.user.entity.user import User as UserEntity
from domain.user.service.user import User as UserService
from infraestructure.user.repository.user import User as UserRepository


class Register:
    user_service = None
    user_repository = None
    my_user = None

    def __init__(self):
        self.user_repository = UserRepository()
        self.user_service = UserService(self.user_repository)

    def register(self, email, password):
        self.my_user = UserEntity(email, password)

        user = self.user_service.register(self.my_user)
        return user
