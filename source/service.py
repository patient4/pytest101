"""

This is a basic microservice whose job is to collect all the data present at any certain endpoint
the purpose of cerating this service is to learn the concept of mocking.
Well explained it in detail in the /tests/test_mockservice.py
"""
import requests
def get_users():
    endpoint = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    raise requests.HTTPError


