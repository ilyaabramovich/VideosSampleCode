from heapq import nlargest
import os
from pathlib import Path
import time


def walk_files_and_sizes(start_at: Path):
    for root, _, files in os.walk(start_at):
        for file in files:
            path = Path(root) / file
            if path.is_file():
                yield path.stat().st_size, path


def largest_files(n: int, start_at: str) -> None:
    start_path = Path(start_at)
    largest = nlargest(n, walk_files_and_sizes(start_path))

    for size, path in largest:
        print(f'{size // (1024 * 1024)} MB {path}')


if __name__ == '__main__':
    start = time.perf_counter()
    largest_files(10, str(Path.home()))
    elapsed = time.perf_counter() - start
    print(f'{elapsed} seconds elapsed')
