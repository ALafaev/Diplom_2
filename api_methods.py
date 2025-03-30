import allure
import requests
from urls import ApiUrls

class ApiMethods:
    @staticmethod
    @allure.step('Создание нового пользователя')
    def create_user(data):
        response = requests.post(ApiUrls.USER_CREATION, data=data)

        return response
