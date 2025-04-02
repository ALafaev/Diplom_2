from data import ExpectedResponse

class CheckResponse:
    @staticmethod
    def check_create_user_response_dict_keys(response):
        response_dict_keys = ExpectedResponse.USER_CREATION_SUCCESSFULLY['response_text_keys']
        return all(key in response_dict_keys for key in response.json().keys())

    @staticmethod
    def check_login_user_response_dict_keys(response):
        response_dict_keys = ExpectedResponse.USER_LOGIN_SUCCESSFULLY['response_text_keys']
        return all(key in response_dict_keys for key in response.json().keys())
