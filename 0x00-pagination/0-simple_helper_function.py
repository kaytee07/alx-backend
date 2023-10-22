#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer argument
page and page_size
"""


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
