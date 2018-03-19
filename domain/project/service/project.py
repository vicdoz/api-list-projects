class Project:
    repository = None

    def __init__(self, project_repository):
        self.repository = project_repository

    def add(self, my_project):
        return self.repository.save(my_project)