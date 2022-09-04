import pytest


@pytest.fixture
def json_request_header():
    header = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    return header

@pytest.fixture
def api_url():
    url = 'https://petstore3.swagger.io/api/v3/pet'
    return url
