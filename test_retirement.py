from retirement import *
from pytest_bdd import given, when, then, parsers, scenario
import mock
import builtins


# Scenario


@scenario('../features/retirement.feature', '1938 as year of birth')
def test_input():
    pass


@when("The user year of birth is 1938 and its month is 2")
def user_input():
    with mock.patch.object(builtins, 'input', lambda _: '1938'):
        assert main() == 65


@then("Results are shown to the user")
def retirement_results():
    pass
