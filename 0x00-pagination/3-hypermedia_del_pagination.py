#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        # Check if index is within the range of dataset
        assert index in range(len(self.dataset()))
        index_dict = self.indexed_dataset()

        # Check if index is 0 and page_size is 10
        if index == 0 and page_size == 10:
            # Get the first 10 elements from index_dict
            data = index_dict[0:10]
        elif index is None:  # Check if index is None
            index = index  # Assign index to itself (redundant statement?)
        # Get the data at the given index from index_dict,
        # or None if index is not present
        data = [index_dict[index] if index in index_dict else None]

        return {
            "index": index,  # Return the index
            "next_index": index + 1,  # Return the next index
            "page_size": page_size,  # Return the page size
            "data": data  # Return the data
        }
