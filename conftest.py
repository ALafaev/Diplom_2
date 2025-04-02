import pytest
import random

@pytest.fixture(scope="function")
def reg_values():
    user_email = f'anton_lafaev_15_{random.randint(1000,9999)}@yandex.ru'
    user_password = 'qwerty'
    user_name = 'Антон'
    return {
        "email": user_email,
        "password": user_password,
        "name": user_name
    }