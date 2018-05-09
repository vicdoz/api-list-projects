class Project:
    repository = None

    def __init__(self, project_repository):
        self.repository = project_repository

    def get(self, my_project=None):
        return self.repository.get(my_project)

    def add(self, my_project):
        return self.repository.save(my_project)
