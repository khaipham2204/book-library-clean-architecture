from __future__ import annotations
import asyncio
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

# ================================================================ #
class AsyncSearchStrategy(ABC):
    @abstractmethod
    async def filter(self, books: list[Book] | None):
        pass

@dataclass
class AsyncTitleSearch(AsyncSearchStrategy):
    keyword : str
    def __post_init__(self):
        self.keyword = self.keyword.lower()

    async def filter(self, books: list[Book] | None):
        await asyncio.sleep(0)
        return list(b for b in books if self.keyword in b.title.lower())

@dataclass
class AsyncAuthorSearch(AsyncSearchStrategy):
    keyword: str
    def __post_init__(self,):
        self.keyword = self.keyword.lower()

    async def filter(self, books: list[Book] | None):
        await asyncio.sleep(0)
        return list(b for b in books if self.keyword in b.author.lower())

