from domain.user.entity.user import User as UserEntity
from domain.user.service.user import User as UserService


class Login:
    user_service = UserService()

    def login(self, email, password):
        my_user = UserEntity(email, password)
        return self.user_service.login(my_user)
