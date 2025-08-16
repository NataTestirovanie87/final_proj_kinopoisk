import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
url_search_film = config['DEFAULT']['url_search_film']


class Advanced_Search():
    """Класс для взаимодействия с расширенным поиском Кинопоиска """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Поиск фильмов по жанру в расширенном поиске")
    def search_film_by_genre(self, target_value: int) -> list:
        with allure.step("Открыть страницу расширенного поиска"):
            self.driver.get(url_search_film)

        with allure.step("Выбрать жанр из селектора"):
            genre_select_element = self.driver.find_element(
                By.CSS_SELECTOR, 'select[name="m_act[genre][]"]')
            select = Select(genre_select_element)
            select.select_by_value(str(target_value))

        with allure.step("Нажать кнопку поиска"):
            search_button = self.driver.find_element(
                By.CSS_SELECTOR, 'input[type="button"][value="поиск"]')
            search_button.click()

        with allure.step("Ожидать появления результатов или изменения URL"):
            wait = WebDriverWait(self.driver, 10)
            try:
                wait.until(EC.url_contains("result="))
            except Exception:
                print("Не удалось дождаться обновления страницы по URL.")

        with allure.step("Получить список фильмов"):
            films_elements = self.driver.find_elements(
                By.CSS_SELECTOR, 'div.search_results .element')

            return films_elements

    @allure.step("Поиск фильмов по стране производства в расширенном поиске")
    def search_film_by_country(self, target_value: int) -> None:
        with allure.step("Открыть страницу расширенного поиска"):
            self.driver.get(url_search_film)

        with allure.step("Выбрать страну из селектора"):
            country_select_element = self.driver.find_element(
                By.CSS_SELECTOR, 'select[name="m_act[country]"]')
            select = Select(country_select_element)
            select.select_by_value(str(target_value))

        with allure.step("Нажать кнопку поиска"):
            search_button = self.driver.find_element(
                By.CSS_SELECTOR, 'input[type="button"][value="поиск"]')
            search_button.click()

        with allure.step("Ожидать появления результатов или изменения URL"):
            wait = WebDriverWait(self.driver, 10)
            try:
                wait.until(EC.url_contains("kinopoisk.ru/lists/m_act"))
            except Exception:
                print("Не удалось дождаться обновления страницы по URL.")

    @allure.step("Поиск фильмов по году производства в расширенном поиске")
    def search_film_by_year(self, target_value: str) -> list:
        with allure.step("Открыть страницу расширенного поиска"):
            self.driver.get(url_search_film)

        with allure.step("Ввести в поле ввода искомый год"):
            year_input = self.driver.find_element(
                By.CSS_SELECTOR, 'input[name="m_act[year]"]')
            year_input.send_keys(target_value)

        with allure.step("Нажать кнопку поиска"):
            search_button = self.driver.find_element(
                By.CSS_SELECTOR, 'input[type="button"][value="поиск"]')
            search_button.click()

        with allure.step("Ожидать появления результатов или изменения URL"):
            wait = WebDriverWait(self.driver, 10)
            try:
                wait.until(EC.url_contains("result="))
            except Exception:
                print("Не удалось дождаться обновления страницы по URL.")

        with allure.step("Получить список фильмов"):
            films_elements = self.driver.find_elements(
                By.CSS_SELECTOR, 'div.search_results .element')

            return films_elements

    @allure.step("Поиск фильмов по компании-прокатчику в расширенном поиске")
    def search_film_by_company(self, target_value: str) -> list:
        with allure.step("Открыть страницу расширенного поиска"):
            self.driver.get(url_search_film)

        with allure.step("Выбрать компанию-прокатчика из селектора"):
            company_select_element = self.driver.find_element(
                By.CSS_SELECTOR, 'select[name="m_act[company]"]')
            select = Select(company_select_element)
            select.select_by_value(str(target_value))

        with allure.step("Нажать кнопку поиска"):
            search_button = self.driver.find_element(
                By.CSS_SELECTOR, 'input[type="button"][value="поиск"]')
            search_button.click()
        with allure.step("Ожидать появления результатов или изменения URL"):
            wait = WebDriverWait(self.driver, 10)
            try:
                wait.until(EC.url_contains("result="))
            except Exception:
                print("Не удалось дождаться обновления страницы по URL.")

        with allure.step("Получить список элементов фильмов"):
            films_elements = self.driver.find_elements(
                By.CSS_SELECTOR, 'div.search_results .element')

            return films_elements

    @allure.step("Поиск фильмов по режиссеру в расширенном поиске")
    def search_film_by_director(self, target_value: int, name: str) -> list:
        with allure.step("Открываем страницу расширенного поиска"):
            self.driver.get(url_search_film)
            self.name = name

        with allure.step("Вводим имя автора в поле ввода"):
            field = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "cr_search_field_1"))
            )
            field.clear()
            field.send_keys(name)

        with allure.step("Выбираем вариант из подсказок автодополнения"):
            try:
                path = (
                    "//ul[contains(@class, 'ui-autocomplete') or "
                    "contains(@class, 'autocomplete')]"
                    "//li[normalize-space()='{n}']"
                ).format(n=name)

                locator = (By.XPATH, path)

                option = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable(locator)
                )
                option.click()
            except Exception:
                # Альтернатива: навигация клавишами
                field.send_keys(Keys.ARROW_DOWN)
                field.send_keys(Keys.ENTER)

        with allure.step("Нажимаем кнопку поиска"):
            search_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#btn_search_6'))
            )
            search_button.click()

        with allure.step("Ждем появления результатов или изменения URL"):
            fragment = "m_act[creator_array]="
            wait = WebDriverWait(self.driver, 10)
            try:
                wait.until(EC.url_contains(fragment))
            except Exception:
                print("Не удалось дождаться обновления страницы по URL.")

        with allure.step("Получаем список элементов фильмов"):
            films_elements = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((
                    By.CSS_SELECTOR, 'div.search_results .element'))
            )
            return films_elements
