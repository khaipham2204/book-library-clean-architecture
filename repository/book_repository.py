from __future__ import annotations
from dataclasses import dataclass, field
from entities.book import Book
from strategy.search_strategy import SearchStrategy

@dataclass
class BookRepository:
    _book: list[Book] = field(default_factory=list)

    def add(self, book: Book):
        self._book.append(book)

    def remove(self, title: str):
        self._book = list(b for b in self._book if b.title != title)

    def get_all(self,):
        return self._book

    def find_by(self, strategy: SearchStrategy):
        return strategy.filter(self._book)

