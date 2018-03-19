from behave import given, when, then


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl_1(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl_2(context):
    assert context.failed is False
