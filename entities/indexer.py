import re
from entities.book import Book
from dataclasses import dataclass, field

@dataclass
class AsyncBookIndexer:
    index: set = field(default_factory=set)
    content_map: dict = field(default_factory=dict)

    def tokenize(self, text: str):
        return re.findall(r'\b\w+\b', text.lower())

    def index_file(self, path: str, content: str):
        self.content_map[path] = content
        list(map(lambda word: self.index[word].add(path),self.tokenize(content)))

    def index_files(self, files: list[Book]):
        for content,index in enumerate(files):
            self.index_file(index, content)


