def assert_films_found(films):
    assert films, "Фильмы не найдены (список равен None или пуст)"
    assert len(films) > 0, "Нет фильмов по заданному жанру"
