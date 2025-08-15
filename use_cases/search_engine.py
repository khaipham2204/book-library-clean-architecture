from dataclasses import dataclass
from entities.indexer import AsyncBookIndexer

@dataclass
class AsyncSearchEngine:
    indexer: AsyncBookIndexer

    async def search(self, keyword: str):
        word = keyword.lower()
        matches = self.indexer.index.get(word, set())
        return {path: self.indexer.content_map[path] for path in matches}
