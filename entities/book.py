from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int

    def __str__(self):
       return f"{self.title} by {self.author} ({self.year})"
