import json

import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    """
    Returns the base URL.
    """
    return "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"


@pytest.fixture(scope="session")
def get_request(base_url):
    response = requests.get(base_url)
    print(f"Requesting URL: {base_url}")
    return response


@pytest.fixture(scope="session")
def get_request_json(get_request):
    """
    Automatically pretty-prints the JSON response for each test.
    """
    data = get_request.json()
    json_formatted = json.dumps(data, indent=2)
    print(json_formatted)
    return data
