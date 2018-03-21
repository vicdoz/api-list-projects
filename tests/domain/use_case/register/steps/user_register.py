from behave import given, when, then
from domain.user.use_case.register import Register as RegisterUseCase

from domain.user.entity.user import User as UserEntity
from unittest.mock import MagicMock
from infraestructure.user.repository.user import User as UserRepository


@given('I try to register a user with username empty and password "{password}"')
@given('I try to register a user with username "{username}" and password empty')
@given('I try to register a user with username "{username}" and password "{password}"')
def new_user_valid(context, username=None, password=None):
    context.email = username
    context.password = password
    try:
        context.my_new_user = UserEntity(username, password)
        context.exc = None
    except Exception as ex:
        context.exc = str(ex)
        context.my_new_user = None


@when('we try to register the user')
def register_user(context):
    # Mocking the repository
    context.user_repository = UserRepository()
    context.user_repository.save = MagicMock(return_value=context.my_new_user)
    register_use_case = RegisterUseCase()
    register_use_case.user_repository = context.user_repository
    register_use_case.user_service.repository = context.user_repository
    try:
        context.user = register_use_case.register(email=context.email, password=context.password)
    except Exception as ex:
        context.exc = str(ex)
        context.my_new_user = register_use_case.my_user


@then('the user is saved')
def check_new_user_saved(context):
    assert context.user == context.my_new_user


@then('the error "{error}" is shown')
def check_new_user_without_any_field(context, error):
    assert context.exc == error

