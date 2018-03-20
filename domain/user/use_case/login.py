from domain.user.entity.user import User as UserEntity
from domain.user.service.user import User as UserService
from infraestructure.user.repository.user import User as user_repository


class Login:
    user_repository = None
    user_service = None

    def __init__(self):
        self.user_repository = user_repository()
        self.user_service = UserService(self.user_repository)

    def login(self, email, password):
        my_user = UserEntity(email, password)
        return self.user_service.login(my_user)
