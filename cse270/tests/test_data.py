import requests

def test_user_endpoint():
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    response = requests.get(url, params=params)

    # Print the response status code
    print(f"Response Status Code: {response.status_code}")

    # Assert the status code
    assert response.status_code == 200

    # Assert the response is empty
    assert response.text == ""

# Run the test
test_user_endpoint()


# Prompts:

# 1.) Please create an integration test in python that calls the endpoint at http://127.0.0.1:8000/users/?username=admin&password=qwerty

# 2.) excellent. Now add a way to verify that the response is HTTP code 200 to the integration test

# 3.) This did not work, as Pytest got an assertion error. The response is expected to be empty. Would this change whether or not the test would work?
