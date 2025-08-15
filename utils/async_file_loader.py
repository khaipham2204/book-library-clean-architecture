import os
import aiofiles
import asyncio

from entities.book import Book

async def async_read_book_file(filepath: str) -> None:
    try:
        async with aiofiles.open(filepath, 'r', encoding='utf-8') as f:
            lines = await f.readlines()
            if len(lines) >= 3:
                title = lines[0].strip()
                author = lines[1].strip()
                year = int(lines[2].strip())
                return Book(title, author, year)
            else:
                print(f"Skipped (not enough lines): {filepath}")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return None


async def async_load_books_from_folder(folderpath: str) -> list[Book]:
    tasks = list(
        map(lambda filename: async_read_book_file(os.path.join(folderpath, filename)) if filename.endswith('.txt') else None,
            os.listdir(folderpath))
    )
    results =  await asyncio.gather(*tasks)
    return list(book for book in results if book is not None)
