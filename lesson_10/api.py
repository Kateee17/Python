import requests
from typing import Dict, Any

class API:
    def __init__(self, base_url: str):
        """
        Инициализация класса API

        :param base_url: Основной URL API (строка)
        """
        self.base_url = base_url

    def create_project(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Создает новый проект

        :param project_data: Данные проекта (словарь)
        :return: Ответ API (словарь)
        """
        response = requests.post(f"{self.base_url}/api-v2/projects", json=project_data)
        return response.json()

    def get_project(self, project_id: int) -> Dict[str, Any]:
        """
        Получает информацию о проекте по ID

        :param project_id: ID проекта (целое число)
        :return: Ответ API (словарь)
        """
        response = requests.get(f"{self.base_url}/api-v2/projects/{project_id}")
        return response.json()

    def update_project(self, project_id: int, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Обновляет проект по ID

        :param project_id: ID проекта (целое число)
        :param project_data: Обновленные данные проекта (словарь)
        :return: Ответ API (словарь)
        """
        response = requests.put(f"{self.base_url}/api-v2/projects/{project_id}", json=project_data)
        return response.json()

    def delete_project(self, project_id: int) -> Dict[str, Any]:
        """
        Удаляет проект по ID

        :param project_id: ID проекта (целое число)
        :return: Ответ API (словарь)
        """
        response = requests.delete(f"{self.base_url}/api-v2/projects/{project_id}")
        return response.json()