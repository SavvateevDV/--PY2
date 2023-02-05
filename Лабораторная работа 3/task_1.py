class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property  # свойство неизменяемости атрибута
    def author(self):
        return (self._author)

    @property  # свойство неизменяемости атрибута
    def name(self):
        return (self._name)

class PaperBook(Book):  # применяем наследование
    def __init__(self, name: str, author: str, pages: int):
        self._name = name
        self._author = author
        self.pages = pages

        if not isinstance(pages, int):  # добавляем ограничения по типу и допустимым значениям
            raise TypeError("Количество страниц должно быть типа int")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"  # добавляем кол-во страниц


class AudioBook(Book):  # применяем наследование
    def __init__(self, name: str, author: str, duration: float):
        self._name = name
        self._author = author
        self.duration = duration

        if not isinstance(duration, float):  # добавляем ограничения по типу и допустимым значениям
            raise TypeError("Количество страниц должно быть типа float")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self.duration}"  # добавляем продол-ость
  # пустая строка