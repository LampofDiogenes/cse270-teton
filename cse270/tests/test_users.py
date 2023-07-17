import requests
import pytest
from unittest import mock




@pytest.mark.integration
def test_get_users_unauthorized(mocker):
    # Set up the test parameters
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Mock the HTTP GET request
    mocker.patch("requests.get")
    requests.get.return_value = mock.Mock(status_code=401, text="")

    # Send the HTTP GET request
    response = requests.get(url, params=params)

    # Assert the response status code
    assert response.status_code == 401

    # Assert the response content is empty
    assert not response.text.strip()

@pytest.mark.integration
def test_get_users_authorized(mocker):
    # Set up the test parameters
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mock the HTTP GET request
    mocker.patch("requests.get")
    requests.get.return_value = mock.Mock(status_code=200, text="")

    # Send the HTTP GET request
    response = requests.get(url, params=params)

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response content is empty
    assert not response.text.strip()
