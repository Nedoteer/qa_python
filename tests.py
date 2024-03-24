from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_genre() ['Что делать, если ваш кот хочет вас убить'] == 'Комедии'



    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Детективы'


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Приключение муравья')
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.set_book_genre('Приключение муравья', 'Мультфильмы')
        assert 'Приключение муравья' in collector.get_books_with_specific_genre('Мультфильмы') and 'Колобок' in collector.get_books_with_specific_genre('Мультфильмы')


    def test_get_books_genre_status(self, books_collector):
        for book in books_collector.books_genre.keys():
            assert book in books_collector.get_books_genre()


    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Ветеран войны с крипами')
        collector.add_new_book('Колобок')
        collector.add_new_book('Алёна в темноте')
        collector.set_book_genre('Ветеран войны с крипами', 'Фантастика')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.set_book_genre('Алёна в темноте', 'Детективы')
        assert 'Ветеран войны с крипами' in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Алёна в темноте')
        collector.add_book_in_favorites('Алёна в темноте')
        assert 'Алёна в темноте' in collector.books_genre and collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.add_book_in_favorites('Колобок')
        collector.delete_book_from_favorites('Колобок')
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize('favorites', ['Алёна в темноте'])
    def test_get_list_of_favorites_books(self, favorites):
        collector = BooksCollector()
        collector.add_new_book('Алёна в темноте')
        collector.add_book_in_favorites(favorites)
        assert favorites in collector.get_list_of_favorites_books()






