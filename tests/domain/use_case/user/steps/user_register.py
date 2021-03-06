from behave import given, when, then
from domain.user.use_case.register import Register as RegisterUseCase

from domain.user.entity.user import User as UserEntity
from unittest.mock import MagicMock
from infraestructure.user.repository.user import User as UserRepository


@given('a user with username empty and password "{password}"')
@given('a user with username "{username}" and password empty')
@given('a user with username "{username}" and password "{password}"')
@given('a user with username empty and password empty')
def new_user_valid(context, username=None, password=None):
    context.email = username
    context.password = password
    context.user_repository = UserRepository()


@when('we try to register the user valid')
def register_user(context):
    context.user_repository.save = MagicMock(return_value=UserEntity(context.email, context.password))
    context.register_use_case = RegisterUseCase()
    context.register_use_case.user_service.repository = context.user_repository
    context.user = context.register_use_case.register(email=context.email, password=context.password)


@when('we try to register the user invalid')
def register_user(context):
    try:
        context.user_repository.save = MagicMock(return_value=UserEntity(context.email, context.password))
        context.register_use_case = RegisterUseCase()
        context.register_use_case.user_service.repository = context.user_repository
        context.user = context.register_use_case.register(email=context.email, password=context.password)
    except Exception as ex:
        context.exc = str(ex)
        context.my_new_user = None


@then('the user is saved')
def check_new_user_saved(context):
    assert context.user.email == context.email
    assert context.user.password == context.password


@then('the error "{error}" is shown')
def check_new_user_without_any_field(context, error):
    assert context.exc == error
