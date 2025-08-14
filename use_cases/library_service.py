from __future__ import annotations
from dataclasses import dataclass
from repository.book_repository import BookRepository
from strategy.search_strategy import SearchStrategy
from entities.book import Book

@dataclass
class LibraryService:
    repository: BookRepository

    def add_book(self, book: Book):
        self.repository.add(book)

    def remove_book(self, title: str):
        self.repository.remove(title)

    def list_books(self):
        return self.repository.get_all()

    def search_books(self, strategy: SearchStrategy):
        return self.repository.find_by(strategy)

