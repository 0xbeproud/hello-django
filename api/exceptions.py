from rest_framework.exceptions import APIException


class ServiceException(APIException):
    status_code = 400

    def __init__(self, code=None, detail=None):
        super().__init__(code, "허용되지 않는 값입니다.")
        self.code = code
        self.detail = detail
        self.more_info = f"https://www.weproud.com/docs/errors/{self.code}"
