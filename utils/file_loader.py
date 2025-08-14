import os
from entities.book import Book

def load_books_from_folder(folder_path) -> list[Book]:
    books = list()
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            full_path = os.path.join(folder_path, filename)
            with open(full_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                if len(lines) >= 3:
                    title = lines[0].strip()
                    author = lines[1].strip()
                    try:
                        year = int(lines[2].strip())
                        books.append(Book(title, author,year))
                    except ValueError:
                        print(f"Invalid year in file: {filename}")
                else:
                    print(f"File {filename} does not have enough lines.")
    return books

