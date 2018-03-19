from domain.project.entity.project import Project as ProjectEntity
from domain.project.service.project import Project as ProjectService


class Create:
    project_service = ProjectService()

    def add(self):
        my_project = ProjectEntity()
        return self.project_service.add(my_project)
