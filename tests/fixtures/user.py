import pytest

from api.models import User


@pytest.fixture(scope='module')
def new_user(app):
    """
    Fixture to create a new user
    :param app: app instance
    :return: a new user instance
    """
    params = {
        'first_name': 'Samuel',
        'last_name': 'Afolaranmi',
        'email': 'somerandomemail@gmail.com',
        'password': 'somesecretpassword',
    }
    return User(**params)
