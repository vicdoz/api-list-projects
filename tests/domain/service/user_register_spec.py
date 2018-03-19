from mamba import description, it, before, context
from expects import expect, equal, raise_error
from doublex import Stub

from domain.user.service.user import User as UserService
from domain.user.entity.user import User as UserEntity

from infraestructure.user.repository.user import User as UserRepository


def callback():
    raise AttributeError('error message')


with description(UserService) as self:
    with before.each:
        self.repository = Stub(UserRepository)

    with description("Register a VALID user with valid domain"):
        with before.each:
            self.entity = UserEntity(
                email="test_register@vicdoz.com",
                password="THE_PASSWORD_SUPERSECURE")
            with self.repository:
                self.repository.save(self.entity).returns(self.entity)

        with it("register the user"):
            result = UserService(self.repository).register(self.entity)
            expect(result).to(equal(self.entity))

    # This is not the way, but the expect assertion can't instanciate an object that raises a exception
    with description("User with invalid domain "):
        with it("with domain = GMAIL.COM"):
            user_entity = UserEntity("test_register@vicdoz.com", "THE_PASSWORD_SUPERSECURE")
            user_entity.email = "test_register@GMAIL.COM"
            expect(user_entity.validate_email).to(raise_error)

    with description("User without any data "):
        with it("without email"):
            user_entity = UserEntity("test@vicdoz.com", "THE_PASSWORD_SUPERSECURE")
            user_entity.email = None
            expect(user_entity.validate_user_has_all_fields).to(raise_error)

        with it("without password"):
            user_entity = UserEntity("test@vicdoz.com", "my_password")
            user_entity.password = None
            expect(user_entity.validate_user_has_all_fields).to(raise_error)
