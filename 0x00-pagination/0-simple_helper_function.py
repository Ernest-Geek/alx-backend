#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    calculates the start and end indices for the pagination

    Args:
        page (int): The page number (1-indexd).
        page-size(int): The number of items per page.

    Returns:
        Tuple: A tuple containing the start and end indices for
        the pagination
    """

    start_index = (page - 1) * page_size
    end_index = start_index + (page_size - 1)
    return start_index, end_index
