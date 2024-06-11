import requests
import pytest


@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgoInstantAnsAPI(): 
    # Arrange
    url = "https://api.duckduckgo.com/?q=python+programming&format=json"

    # Act
    response = requests.get(url, verify = False)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert "Python" in body["AbstractText"]

