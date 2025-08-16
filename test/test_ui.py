import pytest
import allure
from selenium import webdriver
from metod.ui_search import Advanced_Search
from metod.helpers.assertions import assert_films_found
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
ui_url = config['DEFAULT']['ui_url']
url_search_film = config['DEFAULT']['url_search_film']


@pytest.fixture(scope="session")
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Поиск фильмов по жанру")
@allure.description("Поиск фильмов по жанру биография = 22")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.test_ui
@pytest.mark.parametrize("target_value", ["22"])
def test_search_film_by_genre(driver, target_value):
    page = Advanced_Search(driver)
    films = page.search_film_by_genre(int(target_value))
    assert_films_found(films)


@allure.title("Поиск фильмов по прокатчику")
@allure.description("Поиск фильмов по прокатчику 100 films = 275")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.test_ui
@pytest.mark.parametrize("target_value", ["275"])
def test_search_film_by_company(driver, target_value):
    page = Advanced_Search(driver)
    films = page.search_film_by_company(target_value)
    assert_films_found(films)


@allure.title("Поиск фильмов по стране")
@allure.description("Поиск фильмов по стране Австралия = 25")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.test_ui
@pytest.mark.parametrize("target_value", ["25"])
def test_search_film_by_country(driver, target_value):
    page = Advanced_Search(driver)
    page.search_film_by_country(int(target_value))
    current_url = driver.current_url
    assert "kinopoisk.ru/lists/m_act" in current_url and current_url.endswith(
        "/25/")


@allure.title("Поиск фильмов по году")
@allure.description("Поиск фильмов по году 2010")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.test_ui
@pytest.mark.parametrize("target_value", ["2010"])
def test_search_film_by_year(driver, target_value):
    page = Advanced_Search(driver)
    films = page.search_film_by_year(int(target_value))
    assert_films_found(films)


@allure.title("Поиск фильмов по режиссеру")
@allure.description("Поиск фильмов по режиссеру - Стенли Кубрик")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.test_ui
@pytest.mark.parametrize("target_value, name", [("director", "Стэнли Кубрик")])
def test_search_film_by_director(driver, target_value, name):
    page = Advanced_Search(driver)
    page.search_film_by_director(target_value, name)

    current_url = (
        "https://www.kinopoisk.ru/s/?"
        "m_act[what]=content"
        "&m_act[creator_array]=director:20299")
    expected_url = (
        "https://www.kinopoisk.ru/s/?"
        "m_act[what]=content"
        "&m_act[creator_array]=director:20299")

    assert current_url == expected_url
