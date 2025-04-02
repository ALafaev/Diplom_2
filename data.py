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
    USER_LOGIN_SUCCESSFULLY = {
        'status_code': 200,
        'response_text_keys': ['accessToken', 'refreshToken', 'success', 'user']
    }
    USER_LOGIN_INCORRECT_DATA = {
        'status_code': 401,
        'response_text': {
            "success": False,
            "message": "email or password are incorrect"
        }
    }
