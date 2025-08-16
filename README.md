# Документация проекта final_proj_kinopoisk 
automated tests for "Kinopoisk" service

## Описание
Проект содержит набор UI-тестов для расширенного поиска фильмов на Kinopoisk с использованием Selenium WebDriver для Chrome,  набор API-тестов на взаимодействие с Kinopoisk API, а также Allure для отчетности.

## Шаблон для автоматизации тестирования на python

### Проект использует следующие технологии (стеки) и синтаксис:

1. **Python**: Основной язык программирования для написания тестов.
2. **Requests**: Инструмент для автоматизации взаимодействия с API.
3. **Selenium**: Библиотека для автоматизации взаимодействия с веб-браузером.
4. **Pytest**: Фреймворк для написания и запуска тестов.
5. **Allure**: Инструмент для генерации отчетов о выполнении тестов.
6. **Config**: Конфигурация включает параметры окружения и окружения тестов: базовый URL API и веб,  а также токены API.

### Форматирование кода

- Код форматируется в соответствии с PEP 8 (стиль написания кода на Python).
- Используются docstrings для документирования методов и функций.
- Все шаги теста размечаются с помощью `@allure.step` или `with allure.step` для улучшения читаемости отчетов.

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure-pytest
  + Для Windows
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
  + Для macOS
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

### Структура:
- ./test - тесты
- ./metod - классы с методами для API и UI
- ./metod/helpers - хелпер для работы с UI 
- conf.ini - параметры окружения и окружения тестов
- conftest - фискстура для браузера Chrome
- pytest.ini - настройки конфигурации и маркеры 

## Шаги
1. Склонировать проект 'git clone https://github.com/NataTestirovanie87/final_proj_kinopoisk'
2. Установить зависимости 
 ```bash
   pip install -r requirements.txt
   ```
3. Запустить тесты c генерацией отчета в Allure
   ```bash
   pytest --alluredir=./allure-results
   ```
4. Просмотреть отчет 
```bash
   allure serve ./allure-results
   ```
   Эта команда запустит локальный сервер и откроет отчет в браузере.

### В отчете Вы увидите:
- Overview - раздел с общей информацией: сколько всего тестов запустилось, процент успешных тестов, доля успешных и неуспешных тестов.
- Suites - раздел со списком тестов, в котором можно ознакомиться с подробной информацией о каждом тесте (статус, название, серьезность, описание, шаги, тестовые данные)

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Ссылка на финальный проект по ручному тестированию сервиса Кинопоиск]( https://qa-shabardina2025.yonote.ru/share/0bb820ec-fc44-4945-94f0-49eabafb5b21)
