import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2/projects"
HEADERS = {"Authorization": "Bearer 9+cF8a02BG3-TdkiV07OknuhhhNcLXwzXDgewoMu+2Ikz+y8tq1HAV-v6v7M-DZO", "Content-Type": "application/json"}

#РџРѕР·РёС‚РёРІРЅС‹Рµ С‚РµСЃС‚С‹
def test_create_project():
    data = {"title": "New Project"}
    response = requests.post(BASE_URL, headers=HEADERS, json=data)

    assert response.status_code == 201
    assert 'id' in response.json()

def test_get_projects():
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200
    assert 'content' in response.json()

def test_update_project():
#РџСЂРµРґРїРѕР»РѕР¶РёРј, С‡С‚Рѕ РїСЂРѕРµРєС‚ СЃ id = 1 СЃСѓС‰РµСЃС‚РІСѓРµС‚
    project_id = "e00d4ccd-e145-4121-a003-07725ddd41e0"
    update_data = {"title": "Updated Project Name"}
    response = requests.put(f"{BASE_URL}/{project_id}", headers=HEADERS, json=update_data)
    assert response.status_code == 200


def test_get_project():
    project_id = "e00d4ccd-e145-4121-a003-07725ddd41e0"
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['id'] == project_id

#РќРµРіР°С‚РёРІРЅС‹Рµ С‚РµСЃС‚С‹
def test_create_project_without_name():
    data = {"description": "This project has no name"}
    response = requests.post(BASE_URL, headers=HEADERS, json=data)
    assert response.status_code == 400  # РћР¶РёРґР°РµРј РѕС€РёР±РєСѓ

def test_create_project_without_description():
    data = {"name": "Project With No Description"}
    response = requests.post(BASE_URL, headers=HEADERS, json=data)
    assert response.status_code == 400  # РћР¶РёРґР°РµРј РѕС€РёР±РєСѓ