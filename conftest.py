import pytest
from main import BooksCollector


@pytest.fixture
def books_collector():
    collector = BooksCollector()
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.add_new_book('Колобок')
    collector.add_new_book('Приключение муравья')
    collector.add_new_book('Ветеран войны с крипами')
    return collector