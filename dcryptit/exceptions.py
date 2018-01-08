class DcryptItException(IOError):
    """Generic error for when no other exception matches"""

    def __init__(self, *args, **kwargs):
        super(DcryptItException, self).__init__(*args, **kwargs)

class ConnectionError(DcryptItException):
    """An error occurred while connecting to dcrypt.it"""

class APIError(DcryptItException):
    """The response from dcrypt.it is not what we were expecting"""

class HTTPError(DcryptItException):
    """The HTTP request returned an unsuccessful status code"""
