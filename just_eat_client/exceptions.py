from requests.exceptions import ConnectionError


class ConnectionException(ConnectionError):
    pass
