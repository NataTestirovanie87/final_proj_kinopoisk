import requests
import allure


class Kinopoisk_Api:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    @allure.step("Формирование заголовков запроса")
    def get_headers(self) -> dict[str, str]:
        headers = {
            "accept": "application/json"}
        if self.token:
            headers["X-API-KEY"] = self.token
        return headers

    @allure.step("Выполнение GET-запроса с заголовками")
    def get(self, endpoint: str) -> dict[str, str]:
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    @allure.step("Получение информации о фильме по ID")
    def search_movie_by_id(self, film_id: int) -> dict:
        """Метод запрашивает фильм по его id
        Возвращает код 200  при успешном поиске
        Возвращает код 404 при запросе с несуществующим id"""
        url = f"{self.base_url}/api/v2.2/films/{film_id}"
        headers = self.get_headers()
        resp = requests.get(url, headers=headers)
        resp.reise_for_status()
        return resp.json()

    @allure.step("Получение данных актера по имени (URL-кодирование имени)")
    def search_actor_by_name(self, name: str) -> dict:
        """Метод запрашивает данные об актере по его id
        Возвращает код 200  при успешном поиске
        Возвращает код 404 при запросе с несуществующим id
        Требуется URL-кодирование имени актера для запроса на UTF-8"""
        url = f"{self.base_url}/api/v1/persons"
        headers = self.get_headers()
        params = {'name': name}
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        return resp.json()

    @allure.step("Получение информации об актере по ID")
    def search_actor_by_id(self, actor_id: int) -> dict:
        """Метод запрашивает актера по его id
        Возвращает код 200  при успешном поиске
        Возвращает код 404 при запросе с несуществующим id актера"""
        url = f"{self.base_url}/api/v1/staff/{actor_id}"
        headers = self.get_headers()
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp.json()
