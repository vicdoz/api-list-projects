import user.model.user as model
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists, drop_database

from config import Config


def setup_package():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
    if database_exists(engine.url):
        print("Dropping database")
        drop_database(engine.url)
    print("Creating database")

    create_database(engine.url)
    print("Creating tables")
    model.Base.metadata.create_all(engine)
    engine.dispose()


setup_package()
