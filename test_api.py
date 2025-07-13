def test_api_response_status_code(get_request):
    """
    Test to ensure the API response status code is 200 (success).
    """
    assert get_request.status_code == 200


def test_api_response_name(get_request_json):
    """
    Acceptance criteria #1: Ensure the name value is as expected.
    """
    assert get_request_json['Name'] == "Carbon credits"


def test_api_response_can_list(get_request_json):
    """
    Acceptance criteria #2: Ensure the CanRelist value is as expected.
    """
    assert get_request_json['CanRelist'] is True


def test_promotions_description(get_request_json):
    """
    Acceptance criteria #3: Ensure Promotions contains the expected Description - acceptance criteria #3.
    """
    gallery = next((item for item in get_request_json['Promotions'] if item["Name"] == "Gallery"), None)
    assert "Good position in category" in gallery['Description']
