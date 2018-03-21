class User:
    repository = None

    def __init__(self, user_repository):
        self.repository = user_repository

    def login(self, my_user):
        return self.repository.get(my_user)

    def register(self, my_user):
        return self.repository.save(my_user)
