from __future__ import annotations
from dataclasses import dataclass, field
from repository.book_repository import BookRepository
from strategy.search_strategy import SearchStrategy, AsyncSearchStrategy
from entities.book import Book
from entities.observer import Observer

@dataclass
class LibraryService:
    repository: BookRepository
    _observers: list[Observer] = field(default_factory=list)

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def notify_all(self, message: str):
        list(map(lambda observer: observer.update(message),self._observers))

    def add_book(self, book: Book):
        self.repository.add(book)

    def add_book_bulk(self, books: list[Book]):
        self.repository.add_bulk(books)

    def remove_book(self, title: str):
        self.repository.remove(title)

    def list_books(self):
        return self.repository.get_all()

    def search_books(self, strategy: SearchStrategy):
        return self.repository.find_by(strategy)

    async def async_search_books(self, strategies: list[AsyncSearchStrategy]):
        return await self.repository.async_search_books(strategies)
