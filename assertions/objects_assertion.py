
from utilities.files_utils import read_json_test_data



def should_be_match_value(response, request, key):
    # убеждаемся, что объект корректно сохранен на сервере
    value_key_response = response.json()[key]
    value_key_request = read_json_test_data(request)[key]
    assert value_key_response == value_key_request

def should_not_be_match_key(response, key = "run_id"):
    # убеждаемся, что объект корректно сохранен на сервере

    try:
        assert key in response.json()
    except AssertionError:
        return True


