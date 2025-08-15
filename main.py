import asyncio
from use_cases.library_service import LibraryService
from repository.book_repository import BookRepository
from interface_adapters.menu import Menu
from interface_adapters.notifier import ConsoleNotifier, LoggerNotifier
from entities.indexer import AsyncBookIndexer

async def main():
    console = ConsoleNotifier()
    logger = LoggerNotifier()
    indexer = AsyncBookIndexer()
    repository = BookRepository(indexer=indexer)
    service = LibraryService(repository)
    # Attach observers:
    service.add_observer(console)
    service.add_observer(logger)
    service.notify_all("LibraryService")
    menu = Menu(service)
    await menu.display()

if __name__ == "__main__":
    asyncio.run(main())
