from infraestructure.user.repository.user import User as user_repository


class User:
    repository = user_repository()

    def login(self, my_user):
        return self.repository.get_by_email_and_password(my_user)

    def register(self, my_user):
        return self.repository.save(my_user)
