from mamba import description, it, before
from expects import expect, equal
from doublex import Stub

from domain.user.service.user import User as UserService
from domain.user.entity.user import User as UserEntity
from infraestructure.user.repository.user import User as UserRepository

with description(UserService) as self:
    with before.each:
        self.repository = Stub(UserRepository)
        self.entity = UserEntity("test_login@vicdoz.com", "password")

    with description("with no users registered"):
        with before.each:
            with self.repository:
                self.repository.get_by_email_and_password(self.entity).returns([])

        with it("Returns no users"):
            result = UserService(self.repository).login(self.entity)
            expect(result).to(equal([]))

    with description("With one user registered "):
        with before.each:
            self.entity = UserEntity(email="test01@vicdoz.com", password="MY_PASSWORD_123")
            with self.repository:
                self.repository.get_by_email_and_password(self.entity).returns(self.entity)

        with it("Returns no users"):
            result = UserService(self.repository).login(self.entity)
            expect(result).to(equal(self.entity))

    with description("With one user registered,but not match "):
        with before.each:
            self.entity = UserEntity(email="test01@vicdoz.com", password="NOT_VALID_PASSWORD")
            with self.repository:
                self.repository.get_by_email_and_password(self.entity).returns(None)

        with it("Returns no users"):
            result = UserService(self.repository).login(self.entity)
            expect(result).to(equal(None))
