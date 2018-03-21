from domain.user.entity.user import User as UserEntity
from domain.user.service.user import User as UserService
from infraestructure.user.repository.user import User as UserRepository


class Login:
    user_service = None
    user_repository = None
    my_user = None
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_service = UserService(self.user_repository)

    def login(self, email, password):
        self.my_user = UserEntity(email, password)
        return self.user_service.login(self.my_user)
