import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts'
headers = {'content-type': 'application/json; charset=UTF-8'}


def test_get_posts_status_200():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.status_code != 500
    assert response.elapsed.total_seconds() <= 0.8

def test_post():
    data = { 'title': 'brain','body': 'I need a new brain','userId': 125,}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201
    assert response.elapsed.total_seconds() <= 0.8
    assert isinstance(response.json()["id"], int)
    assert response.json()["userId"] == 125

def test_delete():
    response = requests.delete(url+'/1', headers=headers)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() <= 0.8
