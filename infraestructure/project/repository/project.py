from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infraestructure.config import Config
from infraestructure.project.model.project import Project as ProjectModel

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)


class Project:
    db = None

    def __init__(self):
        Session = sessionmaker(bind=engine, autoflush=True, autocommit=False)
        self.db = Session()

    def get(self, project):
        filter_data = self.db.query(ProjectModel)
        project_data = filter_data.one_or_none()
        return project_data

    def save(self, project_entity):
        try:
            project = ProjectModel(
                code=project_entity.code,
                url=project_entity.url,

            )
            self.db.add(project)
            self.db.commit()
            return project_entity
        except Exception:
            self.db.rollback()
            return None
