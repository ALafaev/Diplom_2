import allure
from helpers import CheckResponse
from data import ExpectedResponse
from api_methods import ApiMethods

class TestCreateUser:

    @allure.title('Проверка: можно создать пользователя')
    @allure.description('Запрос POST на /api/auth/register с валидными данными вернет 200 OK')
    def test_user_creation_with_valid_data_return_200_ok(self, reg_values):
        response = ApiMethods.create_user(reg_values)

        assert (response.status_code == ExpectedResponse.USER_CREATION_SUCCESSFULLY['status_code']
                and CheckResponse.check_create_user_response_dict_keys(response)), "Ответ сервера не совпадает с ожидаемым"
        token = response.json()["accessToken"]
        ApiMethods.delete_user(token)

    @allure.title('Проверка: нельзя создать пользователя, который уже зарегистрирован')
    @allure.description('Повторный запрос POST на /api/auth/register с теми же данными вернет 403 Forbidden')
    def test_user_creation_with_the_same_data_return_403_forbidden(self, reg_values):
        ApiMethods.create_user(reg_values)
        response = ApiMethods.create_user(reg_values)

        assert (response.status_code == ExpectedResponse.USER_CREATION_ALSO_EXIST['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_ALSO_EXIST['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать пользователя, не передав значение для поля email')
    @allure.description('Запрос POST на /api/auth/register без значения для поля email вернет 403 Forbidden')
    def test_user_creation_without_email_value_return_403_forbidden(self, reg_values):
        reg_data_without_email_value = {
        "email": '',
        "password": reg_values["password"],
        "name": reg_values["name"]
    }
        response = ApiMethods.create_user(reg_data_without_email_value)

        assert (response.status_code == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать пользователя, не передав значение для поля password')
    @allure.description('Запрос POST на /api/auth/register без значения для поля password вернет 403 Forbidden')
    def test_user_creation_without_password_value_return_403_forbidden(self, reg_values):
        reg_data_without_password_value = {
        "email": reg_values["email"],
        "password": '',
        "name": reg_values["name"]
    }
        response = ApiMethods.create_user(reg_data_without_password_value)

        assert (response.status_code == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать пользователя, не передав значение для поля name')
    @allure.description('Запрос POST на /api/auth/register без значения для поля name вернет 403 Forbidden')
    def test_user_creation_without_name_value_return_403_forbidden(self, reg_values):
        reg_data_without_name_value = {
        "email": reg_values["email"],
        "password": reg_values["password"],
        "name": ''
    }
        response = ApiMethods.create_user(reg_data_without_name_value)

        assert (response.status_code == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать пользователя при отсутствии в запросе поля email')
    @allure.description('Запрос POST на /api/auth/register без поля email вернет 403 Forbidden')
    def test_user_creation_without_email_field_return_403_forbidden(self, reg_values):
        reg_data_without_email_field = {
        "password": reg_values["password"],
        "name": reg_values["name"]
    }
        response = ApiMethods.create_user(reg_data_without_email_field)

        assert (response.status_code == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать пользователя при отсутствии в запросе поля password')
    @allure.description('Запрос POST на /api/auth/register без поля password вернет 403 Forbidden')
    def test_user_creation_without_password_field_return_403_forbidden(self, reg_values):
        reg_data_without_password_field = {
        "email": reg_values["email"],
        "name": reg_values["name"]
    }
        response = ApiMethods.create_user(reg_data_without_password_field)

        assert (response.status_code == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"

    @allure.title('Проверка: нельзя создать пользователя при отсутствии в запросе поля name')
    @allure.description('Запрос POST на /api/auth/register без поля name вернет 403 Forbidden')
    def test_user_creation_without_name_field_return_403_forbidden(self, reg_values):
        reg_data_without_name_field = {
        "email": reg_values["email"],
        "password": reg_values["password"]
    }
        response = ApiMethods.create_user(reg_data_without_name_field)

        assert (response.status_code == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['status_code']
                and response.json() == ExpectedResponse.USER_CREATION_WITHOUT_REQUIRED_DATA['response_text']), "Ответ сервера не совпадает с ожидаемым"
