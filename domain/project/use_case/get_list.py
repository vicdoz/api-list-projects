from domain.project.service.project import Project as ProjectService
from infraestructure.project.repository.project import Project as ProjectRepository


class GetList:
    project_service = None
    project_repository = None

    def __init__(self):
        self.project_repository = ProjectRepository()
        self.project_service = ProjectService(self.project_repository)

    def get_list(self):
        return self.project_service.get(self.project_repository)
