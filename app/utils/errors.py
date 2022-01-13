

class BaseError(Exception):
    message = 'base error'

    def __init__(self, message=None):
        if message:
            self.message = message
        super(BaseError, self).__init__()


class JsonError(BaseError):
    message = 'json parse faild'
