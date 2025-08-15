from __future__ import annotations
import asyncio

from dataclasses import dataclass, field
from entities.book import Book
from entities.indexer import AsyncBookIndexer
from strategy.search_strategy import SearchStrategy, AsyncSearchStrategy

@dataclass
class BookRepository:
    indexer: AsyncBookIndexer | None
    _book: list[Book] = field(default_factory=list)

    def add(self, book: Book):
        self._book.append(book)

    def add_bulk(self, books: list[Book]):
        list(map(lambda book: self.add(book),books))

    def remove(self, title: str):
        self._book = list(b for b in self._book if b.title != title)

    def get_all(self,):
        return self._book

    def find_by(self, strategy: SearchStrategy):
        return strategy.filter(self._book)

    async def async_search_books(self, strategies: list[AsyncSearchStrategy]) -> list[Book]:
        tasks: list = [ strategy.filter(self.get_all())  for strategy in strategies ]
        results = await asyncio.gather(*tasks)
        flat = [book for sublist in results for book in sublist]
        seen = set()
        uniques_books = list()
        for book in flat:
            key =  (book.title.lower(), book.author.lower())
            if key not in seen:
                seen.add(key)
                uniques_books.append(book)
        return uniques_books

    def book_indexer(self):
        self.indexer.index_files(self._book)

    async def search_engine(self, keyword: str):
        word = keyword.lower()
        matches = self.indexer.index.get(word, set())
        return {path: self.indexer.content_map[path] for path in matches}

