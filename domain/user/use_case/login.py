from domain.user.entity.user import User as UserEntity
from domain.user.service.user import User as UserService


class Login:
    user_repository = None
    user_service = None

    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.user_service = UserService(user_repository)

    def login(self, email, password):
        my_user = UserEntity(email, password)
        return self.user_service.login(my_user)
