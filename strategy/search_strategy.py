from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from entities.book import Book

class SearchStrategy(ABC):
    @abstractmethod
    def filter(self, books: list[Book] | None):
        pass
@dataclass
class TitleSearch(SearchStrategy):
    keyword : str
    def __post_init__(self):
        self.keyword = self.keyword.lower()

    def filter(self, books: list[Book] | None):
        return list(b for b in books if self.keyword in b.title.lower())

@dataclass
class AuthorSearch(SearchStrategy):
    keyword: str
    def __post_init__(self,):
        self.keyword = self.keyword.lower()

    def filter(self, books: list[Book] | None):
        return list(b for b in books if self.keyword in b.author.lower())

