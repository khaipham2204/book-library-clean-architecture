import asyncio
from dataclasses import dataclass
from strategy.search_strategy import TitleSearch, AuthorSearch, AsyncTitleSearch, AsyncAuthorSearch
from use_cases.library_service import LibraryService

@dataclass
class Menu:
    service: LibraryService

    async def display(self):
        while True:
            print("\n--- Book Library ---")
            print("1. List all books")
            print("2. Add book")
            print("3. Remove book")
            print("4. Search by title")
            print("5. Search by author")
            print("6. Load books from folder")
            print("7. Async search (title + author)")
            print("0. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.list_books()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.remove_book()
            elif choice == "4":
                self.search_by_title()
            elif choice == "5":
                self.search_by_author()
            elif choice == "6":
                self.load_books_from_folder()
            elif choice == "7":
                await self.search_combine_async()
            elif choice == "0":
                break

    def list_books(self,):
        books = self.service.list_books()
        if not books:
            ("No book in librady.")
        for book in books:
            print(book)

    def add_book(self,):
        title = input("Title:")
        author = input("Author: ")
        year = int(input("Year: "))
        from entities.book import Book
        self.service.add_book(Book(title, author, year))

    def remove_book(self):
        title = input("Enter title to remove: ")
        self.service.remove_book(title)

    def search_by_title(self):
        keyword = input("Search title: ")
        result = self.service.search_books(TitleSearch(keyword))
        for book in result:
            print(book)

    def search_by_author(self):
        keyword = input("Search author: ")
        result = self.service.search_books(AuthorSearch(keyword))
        for book in result:
            print(book)

    async def search_combine_async(self,):
        keyword = input("Search keyword (will check title & author): ")
        strategies = [AsyncTitleSearch(keyword), AsyncAuthorSearch(keyword)]
        results = await self.service.async_search_books(strategies)
        list(map(lambda book: print(book) ,results))


    def load_books_from_folder(self):
        from utils.file_loader import load_books_from_folder
        folder = input("Enter folder path: ").strip() or "data"
        books = load_books_from_folder(folder)
        self.service.add_book_bulk(books)

