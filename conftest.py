import logging
import os
from http import HTTPStatus

import pytest
from dotenv import load_dotenv

from api.api_client import ApiClient, ApiClientAsync
from api.objects_api import post_object,  get_object
from assertions.assertion_base import assert_status_code

from utilities.files_utils import read_json_common_request_data
from utilities.logger_utils import logger


def pytest_configure(config):
    # устанавливаем текущую директорию на корень проекта (это позволит прописывать относительные пути к файлам)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # загружаем переменные-параметры из файла /.env
    load_dotenv(dotenv_path=".env")

    # задаем параметры логгера
    path = "logs/"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    file_handler = logging.FileHandler(path + "/info.log", "w")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter("%(lineno)d: %(asctime)s %(message)s"))

    # создаем кастомный логгер
    custom_logger = logging.getLogger("custom_loger")
    custom_logger.setLevel(logging.INFO)
    custom_logger.addHandler(file_handler)


def pytest_runtest_setup(item):
    logger.info(f"{item.name}:")



@pytest.fixture(scope='function')
def value_run_id():
    with ApiClient() as client:
        param = read_json_common_request_data("routes_api")["post_route"]
        # send request
        response = post_object(client, param)
        # check status code
        assert_status_code(response, HTTPStatus.OK)
        # match schema
        value_run_id = response.json()['run_id']
        yield value_run_id





