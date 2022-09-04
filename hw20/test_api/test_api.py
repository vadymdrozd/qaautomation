import requests
from hw20.test_data import test_json
import pytest


def pytest_generate_tests(metafunc):
    if 'test_json_positive_post' in metafunc.function.__name__:
        test_data = test_json.test_json_positive_post
        metafunc.parametrize('positive_request, response', test_data)
    if 'test_json_negative_post' in metafunc.function.__name__:
        test_data = test_json.test_json_negative_post
        metafunc.parametrize('negative_request, status_code', test_data)
    if 'test_json_positive_put' in metafunc.function.__name__:
        test_data = test_json.test_json_positive_put
        metafunc.parametrize('positive_request_body, response', test_data)
    if 'test_json_negative_put' in metafunc.function.__name__:
        test_data = test_json.test_json_negative_put
        metafunc.parametrize('negative_request_body, status_code', test_data)
    if 'test_json_positive_get' in metafunc.function.__name__:
        test_data = test_json.test_json_positive_get
        metafunc.parametrize('positive_request_parameter, status_code', test_data)
    if 'test_json_negative_get' in metafunc.function.__name__:
        test_data = test_json.test_json_negative_get
        metafunc.parametrize('negative_request_parameter, status_code', test_data)


class TestPetApi:

    def test_json_positive_post_pet(self, api_url, json_request_header, positive_request, response):
        headers = json_request_header
        pet_request_body = positive_request
        expected_response = response
        new_pet = requests.post(f'{api_url}', json=pet_request_body, headers=headers)
        assert new_pet.json() == expected_response, f'Incorrect server response - {new_pet.json()}.' \
                                                    f'Should be {expected_response}'
        assert new_pet.status_code == 200, f'Incorrect status code - {new_pet.status_code}. Should be 200'

    def test_json_negative_post_pet(self, api_url, json_request_header, negative_request, status_code):
        headers = json_request_header
        pet_request_body = negative_request
        expected_status_code = status_code
        new_pet = requests.post(f'{api_url}', json=pet_request_body, headers=headers)
        assert new_pet.status_code == expected_status_code, f'Incorrect status code - {new_pet.status_code}.' \
                                                            f'Should be {expected_status_code}'

    def test_json_positive_put_pet(self, api_url, json_request_header, positive_request_body, response):
        header = json_request_header
        pet_request_body = positive_request_body
        pet_response_body = response
        updated_pet = requests.put(f'{api_url}', json=pet_request_body, headers=header)
        assert updated_pet.status_code == 200
        assert updated_pet.json() == pet_response_body

    def test_json_negative_put_pet(self, api_url, json_request_header, negative_request_body, status_code):
        header = json_request_header
        pet_request_body = negative_request_body
        expected_status_code = status_code
        updated_pet = requests.put(f'{api_url}', json=pet_request_body, headers=header)
        assert updated_pet.status_code == status_code, f'Incorrect status code - {updated_pet.status_code}.' \
                                                       f'Should be {expected_status_code}'

    def test_json_positive_get_find_by_status(self, api_url, json_request_header, positive_request_parameter, status_code):
        header = json_request_header
        request = requests.get(f'{api_url}/findByStatus?status={positive_request_parameter}', headers=header)
        expected_status_code = status_code
        assert request.status_code == expected_status_code, f'Incorrect status code - {request.status_code}.' \
                                                            f'Should be {expected_status_code}'

    def test_json_negative_get_find_by_status(self, api_url, json_request_header, negative_request_parameter, status_code):
        header = json_request_header
        request = requests.get(f'{api_url}/findByStatus?status={negative_request_parameter}', headers=header)
        expected_status_code = status_code
        assert request.status_code == expected_status_code, f'Incorrect status code - {request.status_code}.' \
                                                            f'Should be {expected_status_code}'
