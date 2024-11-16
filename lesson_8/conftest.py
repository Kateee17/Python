import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2/projects"
HEADERS = {"Authorization": "H6HngIA816fpIhY7tBvWx/it3YbVvEt/33Sk8afA39MCR9a", "Content-Type": "application/json"}
#Позитивные тесты
def test_create_project():
data = {"name": "New Project",
        "description": "Project created for testing"}
response = requests.post(BASE_URL, headers=HEADERS, json=data)
assert response.status_code == 201
assert response.json()['name'] == data['name']

def test_get_projects():
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_project():
#Предположим, что проект с id = 1 существует
    project_id = 1
    update_data = {"name": "Updated Project Name"}
    response = requests.put(f"{BASE_URL}/{project_id}", headers=HEADERS, json=update_data)
    assert response.status_code == 200
    assert response.json()['name'] == update_data['name']

def test_get_project():
    project_id = 1
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['id'] == project_id

#Негативные тесты
def test_create_project_without_name():
    data = {"description": "This project has no name"}
    response = requests.post(BASE_URL, headers=HEADERS, json=data)
    assert response.status_code == 400  # Ожидаем ошибку

def test_create_project_without_description():
    data = {"name": "Project With No Description"}
    response = requests.post(BASE_URL, headers=HEADERS, json=data)
    assert response.status_code == 400  # Ожидаем ошибку
if __name__ == "__main__":
    pytest.main()