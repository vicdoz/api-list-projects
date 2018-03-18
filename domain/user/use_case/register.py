from domain.user.entity.user import User as UserEntity
from domain.user.service.user import User as UserService


class Register:
    user_service = UserService()

    def register(self, email, password):
        my_user = UserEntity(email, password)
        my_user.validate_email()
        return self.user_service.register(my_user)
