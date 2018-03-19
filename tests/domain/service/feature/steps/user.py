from behave import given, when, then
from domain.user.service.user import User as UserService
from domain.user.entity.user import User as UserEntity
from unittest.mock import MagicMock
from infraestructure.user.repository.user import User as UserRepository


@given('a new VALID user')
def new_user_valid(context):
    context.my_new_user = UserEntity("test2321@vicdoz.com", "PASSWORD_TEST")


@when('we register the user')
def register_user(context):
    # Mocking the repository
    context.user_repository = UserRepository()
    context.user_repository.save = MagicMock(return_value=context.my_new_user)

    user_service = UserService(context.user_repository)
    context.user = user_service.register(context.my_new_user)


@then('the user is saved')
def check_new_user_saved(context):
    assert context.user == context.my_new_user


@given('a new INVALID user')
def new_user_invalid(context):
    try:
        context.my_new_user = UserEntity("test2321@NOTVALIDDOMAIN.com", "PASSWORD_TEST")
        context.exc = None
    except Exception as ex:
        context.exc = str(ex)
        context.my_new_user = None


@then('the domain is not allowed and the user is not created')
def check_new_user_not_saved(context):
    assert context.exc == "Not allowed domain for this user"
