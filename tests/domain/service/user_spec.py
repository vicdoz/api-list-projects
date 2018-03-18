from mamba import description, it, before
from expects import expect, equal
from doublex import Stub

from domain.user.service.user import User as UserService
from domain.user.entity.user import User as UserEntity
from infraestructure.user.repository.user import User as UserRepository

with description(UserService) as self:
    with before.each:
        self.repository = Stub(UserRepository)
        self.entity = UserEntity("email", "password")

    with description("with no users registered"):
        with before.each:
            with self.repository:
                self.repository.get_by_email_and_password(self.entity).returns([])

        with it("Returns no users"):
            result = UserService(self.repository).login(self.entity)
            expect(result).to(equal([]))
