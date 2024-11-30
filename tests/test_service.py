import unittest.mock as mock
import pytest

import requests

import source.service as service
"""
You see we have imported unittest in a pytest101 tutorial
this is because unittest can be used in pytest directly that's the beauty of pytest
we can literally use other frameworks directly as per our usecases.

What is Mocking?
suppose you have a long running task which depends on some other tasks and so on.
it's better to lay down everything as mocked. by mockin we are saying the test that 
Hey, I am adding this object in @mock.patch("requests.get") please mock it I will be defining 
HOW you mock it.


"""


@mock.patch('requests.get')
def test_get_users(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'message': 'OK', 'name': '<NAME>'}
    data = service.get_users()
    assert data == {'message': 'OK', 'name': '<NAME>'}

@mock.patch('requests.get')
def test_get_users_error(mock_get):
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {'message': 'Something went wrong'}
    with pytest.raises(requests.exceptions.HTTPError):
        data = service.get_users()
