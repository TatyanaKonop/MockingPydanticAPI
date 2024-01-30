from http import HTTPStatus
from idlelib.multicall import r

import polling2

from api.api_client import ApiClient
from api.objects_api import get_object
from assertions.assertion_base import assert_status_code, assert_schema
from assertions.objects_assertion import  should_not_be_match_key
from models.get_response_model import GetResponseSchema
from utilities.files_utils import read_json_common_request_data


class TestObjectsGet:
    """
    Tests/objects
    """

    def test_get_objects_id_param(self):
        with ApiClient() as client:
            # retrieve routes for test
            param = read_json_common_request_data("routes_api")["get_route"]
            # send request
            response = get_object(client, param)
            # check status code
            assert_status_code(response, HTTPStatus.OK)
            # match schema
            assert_schema(response, GetResponseSchema)

    def test_polling_while_id_not_disappear(self,  value_run_id):
        with ApiClient() as client:
        # retrieve routes for test
            param = read_json_common_request_data("routes_api")["get_route_process"]
            # send request
            polling2.poll(lambda: get_object(client, param),
                                  check_success=lambda response: response.json()["run_id"] != value_run_id if "run_id" in response.json() else True,
                                  step=1,
                                  timeout=0)

    def test_polling_while_key_not_disappear(self,  value_run_id):
        with ApiClient() as client:
            # retrieve routes for test
            param = read_json_common_request_data("routes_api")["get_route_process"]
            # send request
            polling2.poll(lambda: get_object(client, param),
                          check_success= should_not_be_match_key,
                          step=1,
                          timeout=0)

