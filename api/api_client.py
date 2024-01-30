import os
from httpx import Client, Response, AsyncClient
from utilities.logger_utils import logger


class ApiClient(Client):
    """
    Extend standart httpx client
    """

    def __init__(self):
        super().__init__(base_url=f"http://{os.getenv('RESOURSE_URL')}")


    def request(self, method, url, **kwargs) -> Response:
        """
        extent logic httpx method - add logging with name request and its url
        logging is defined in .env
        :param method: (POST, GET и.т.д)
        :param url: domen name
        """

        if eval(os.getenv("USE_LOGS")):
            logger.info(f'{method} {url}')
        return super().request(method, url, **kwargs)


class ApiClientAsync(AsyncClient):
    """
    Extend standart httpx client
    """

    def __init__(self):
        super().__init__(base_url=f"http://{os.getenv('RESOURSE_URL')}")


    def request(self, method, url, **kwargs) -> Response:
        """
        extent logic httpx method - add logging with name request and its url
        logging is defined in .env
        :param method: (POST, GET и.т.д)
        :param url: domen name
        """

        if eval(os.getenv("USE_LOGS")):
            logger.info(f'{method} {url}')
        return super().request(method, url, **kwargs)
