class LoginValues:
    NAME = "Антон"
    EMAIL = f'anton_lafaev_15_573@yandex.ru',
    PASSWORD = 'qwerty'

class ExpectedResponse:
    USER_CREATION_SUCCESSFULLY = {
        'status_code':200,
        'response_text_keys':['accessToken', 'refreshToken', 'success', 'user']
    }
    USER_CREATION_ALSO_EXIST = {
        'status_code':403,
        'response_text':{
            "success": False,
            "message": "User already exists"
        }
    }
    USER_CREATION_WITHOUT_REQUIRED_DATA = {
        'status_code': 403,
        'response_text': {
            "success": False,
            "message": "Email, password and name are required fields"
        }
    }

