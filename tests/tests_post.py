from http import HTTPStatus
from api.api_client import ApiClient
from api.objects_api import post_object
from assertions.assertion_base import assert_status_code, assert_schema
from models.post_response_model import PostResponseSchema
from utilities.files_utils import read_json_common_request_data


class TestObjectsPost:
    """
    Tests/objects
    """

    def test_post_object_with_full_body(self):
        """
        create object

        """
        with ApiClient() as client:
            # retrieve routes for test
            param = read_json_common_request_data("routes_api")["post_route"]
            # send request
            response = post_object(client, param)
            # check status code
            assert_status_code(response, HTTPStatus.OK)
            # match schema
            assert_schema(response, PostResponseSchema)
