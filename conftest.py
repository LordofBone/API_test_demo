import json

import pytest
import requests

"""
Everything under here is scoped to the session, so that it only runs once per test session.
Then we access the data from the API request for each test, without having to hit the API multiple times.
"""

@pytest.fixture(scope="session")
def base_url():
    """
    Returns the base URL - put this here so the URL is cleanly documented in code as a fixture.
    """
    return "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"


@pytest.fixture(scope="session")
def get_request(base_url):
    """
    Makes a GET request to the provided base URL and returns the response - base response unformatted, for checking
    status etc.
    """
    response = requests.get(base_url)
    print(f"Requesting URL: {base_url}")
    return response


@pytest.fixture(scope="session")
def get_request_json(get_request):
    """
    Automatically pretty-prints the JSON response for each test - can use this for tests that require validation of the
    responses content.
    """
    data = get_request.json()
    json_formatted = json.dumps(data, indent=2)
    print(json_formatted)
    return data
