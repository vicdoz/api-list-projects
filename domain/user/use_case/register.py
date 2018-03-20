from domain.user.entity.user import User as UserEntity
from domain.user.service.user import User as UserService
from infraestructure.user.repository.user import User as user_repository


class Register:
    user_service = None
    user_repository = None

    def __init(self):
        self.user_repository = user_repository()
        self.user_service = UserService(self.user_repository)

    def register(self, email, password):
        my_user = UserEntity(email, password)
        my_user.validate_email()
        return self.user_service.register(my_user)
