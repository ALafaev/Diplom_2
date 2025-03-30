import pytest
import random
from data import ExpectedResponse

user_email = f'anton_lafaev_15_{random.randint(100,999)}@yandex.ru'
user_password = 'qwerty'
user_name = 'Антон'

class UserData:
    creation_data = {
        "email": user_email,
        "password": user_password,
        "name": user_name
    }
    creation_data_without_email_value = {
        "email": '',
        "password": user_password,
        "name": user_name
    }
    creation_data_without_password_value = {
        "email": user_email,
        "password": '',
        "name": user_name
    }
    creation_data_without_name_value = {
        "email": user_email,
        "password": user_password,
        "name": ''
    }
    creation_data_without_email_field = {
        "password": user_password,
        "name": user_name
    }
    creation_data_without_password_field = {
        "email": user_email,
        "name": user_name
    }
    creation_data_without_name_field = {
        "email": user_email,
        "password": user_password
    }

class CheckUserCreationResponse:
    @staticmethod
    def check_create_user_response_dict_keys(response):
        response_dict_keys = ExpectedResponse.USER_CREATION_SUCCESSFULLY['response_text_keys']
        return all(key in response_dict_keys for key in response.json().keys())
