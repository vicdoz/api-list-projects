from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker

from domain.user.repository_interface.user_interface import UserInterface
from infraestructure.config import Config
from infraestructure.user.model.user import User as UserModel

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)


class User(UserInterface):
    db = None

    def __init__(self):
        UserInterface.__init__(self)
        Session = sessionmaker(bind=engine, autoflush=True, autocommit=False)
        self.db = Session()

    def get_by_email_and_password(self, user_entity):
        filter_data = self.db.query(UserModel).filter(
            and_(
                (user_entity.email == UserModel.email),
                (user_entity.password == UserModel.hash))
        )
        user_data = filter_data.one_or_none()
        return user_data

    def get(self, entity):
        return self.get_by_email_and_password(entity)


    def save(self, user_entity):
        try:
            user = UserModel(
                email=user_entity.email,
                password=user_entity.password
            )
            self.db.add(user)
            self.db.commit()
            return user_entity
        except Exception:
            self.db.rollback()
            return None
