 #!/usr/bin/env python3
"""
a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """
    get the return a tuple of size two containing a start index
    and an end index

    Args:
        page(int): this is the current page
        page_size(int): this is the size of the page

    Return:
        Return: tuple containing start index and an end index
    """
    if page == 0 or page_size == 0:
        return
    start_index = (page * page_size) - page_size
    end_index = page * page_size
    start_end = (start_index, end_index)
    return start_end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get dataset from page and page_size
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        if start_index > len(self.dataset()):
            return []
        return self.dataset()[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """
        get dataset using hypermedia pagination
        """
        page_data = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end_index < len(self.__dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total_pages': total_pages,
        }
