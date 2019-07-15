from rest_framework.exceptions import APIException


class ServiceException(APIException):
    status_code = 400

    def __init__(self, detail=None, code=None):
        super().__init__("허용되지 않는 값입니다.", code)
        self.code = code
        self.detail = detail
        self.more_info = f"https://www.weproud.com/docs/errors/{self.code}"


class UserDoesNotExistException(ServiceException):
    status_code = 400

    def __init__(self, user_id):
        super().__init__(f"{user_id}에 해당하는 User를 찾을 수 없습니다.", 400)
