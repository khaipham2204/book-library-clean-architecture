from use_cases.library_service import LibraryService
from repository.book_repository import BookRepository
from interface_adapters.menu import Menu

def main():
    repository = BookRepository()
    service = LibraryService(repository)
    menu = Menu(service)
    menu.display()

if __name__ == "__main__":
   main()
