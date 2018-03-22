from behave import given, when, then
from domain.project.use_case.get_list import GetList as GetListUseCase
from unittest.mock import MagicMock
from infraestructure.project.repository.project import Project as ProjectRepository


@given('no projects')
def given_condition(context):
    context.project_repository = ProjectRepository()
    context.project_repository.get = MagicMock(return_value=[])
    context.get_project_list_use_case = GetListUseCase()
    context.get_project_list_use_case.project_service.repository = context.project_repository

@given('one project at database')
def given_condition(context):
    context.project_repository = ProjectRepository()
    context.project_repository.get = MagicMock(return_value=[])
    context.get_project_list_use_case = GetListUseCase()
    context.get_project_list_use_case.project_service.repository = context.project_repository

@when('we request a list')
def request_empty_project_list(context):
    context.projects = context.get_project_list_use_case.get_list()


@then('no project is returned')
def check_new_project_saved(context):
    assert len(context.projects) == 0
