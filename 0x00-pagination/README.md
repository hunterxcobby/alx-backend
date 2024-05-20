# Project: 0x00. Pagination

## Resources

### Read or watch:-

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Pagination in Python

This project aims to implement pagination functionality in Python, allowing you to paginate through a dataset efficiently. Pagination is a common requirement in web applications when displaying large sets of data.

## Table of Contents

1. [Simple Helper Function](#simple-helper-function)
2. [Simple Pagination](#simple-pagination)
3. [Hypermedia Pagination](#hypermedia-pagination)
4. [Deletion-Resilient Hypermedia Pagination](#deletion-resilient-hypermedia-pagination)

---

## Simple Helper Function

### Function Description

The `index_range` function takes two integer arguments, `page` and `page_size`. It returns a tuple containing a start index and an end index that correspond to the range of indexes to return in a list for those specific pagination parameters.

- Page numbers are 1-indexed, meaning the first page is referred to as page 1.

### Example Usage

```python
# Import the index_range function
index_range = __import__('0-simple_helper_function').index_range

# Example 1
res = index_range(1, 7)
print(type(res))
print(res)
# Output: <class 'tuple'>, (0, 7)

# Example 2
res = index_range(page=3, page_size=15)
print(type(res))
print(res)
# Output: <class 'tuple'>, (30, 45)
```

---

## Simple Pagination

### Class Description

This section implements simple pagination functionality by defining a `Server` class that can paginate through a database of popular baby names. The class allows you to retrieve a specific page of data based on page number and page size.

### Usage

- The `get_page` method of the `Server` class takes two integer arguments, `page` (default 1) and `page_size` (default 10). It returns a list of lists representing the dataset for the requested page.

- Asserts are used to validate that both `page` and `page_size` are integers greater than 0.

- If the input arguments are out of range for the dataset, an empty list is returned.

Example Usage:

```python
# Import the Server class
Server = __import__('1-simple_pagination').Server

# Create a Server instance
server = Server()

# Example 1: Pagination with valid values
print(server.get_page(1, 3))

# Example 2: Pagination with invalid values (out of range)
print(server.get_page(3000, 100))
```

---

## Hypermedia Pagination

### Class Description

This section extends the pagination functionality by implementing hypermedia pagination. It introduces a `get_hyper` method within the `Server` class that returns pagination information in a dictionary.

### Usage

- The `get_hyper` method takes the same arguments as `get_page` and returns a dictionary with the following key-value pairs:
  - `page_size`: The length of the returned dataset page.
  - `page`: The current page number.
  - `data`: The dataset page.
  - `next_page`: The number of the next page (None if no next page).
  - `prev_page`: The number of the previous page (None if no previous page).
  - `total_pages`: The total number of pages in the dataset as an integer.

- The `get_hyper` method internally uses the `get_page` method for data retrieval.

Example Usage:

```python
# Import the Server class
Server = __import__('2-hypermedia_pagination').Server

# Create a Server instance
server = Server()

# Example: Retrieve hypermedia pagination information
print(server.get_hyper(1, 2))
```

---

## Deletion-Resilient Hypermedia Pagination

### Class Description

This section enhances the hypermedia pagination to be deletion-resilient. The goal is to ensure that if certain rows are removed from the dataset between two queries, the user does not miss any items when changing pages.

### Usage

- The `get_hyper_index` method takes two integer arguments, `index` (default None) and `page_size` (default 10). It returns a dictionary containing pagination information.

- The dictionary includes the following key-value pairs:
  - `index`: The current start index of the return page.
  - `next_index`: The next index to query.
  - `page_size`: The current page size.
  - `data`: The actual page of the dataset.

- The `indexed_dataset` method is used to cache the dataset and index it by sorting position, starting at 0.

- Assertions are used to verify that `index` is in a valid range.

Example Usage:

```python
# Import the Server class
Server = __import__('3-hypermedia_del_pagination').Server

# Create a Server instance
server = Server()

# Example: Retrieve deletion-resilient hypermedia pagination information
print(server.get_hyper_index(3, 2))
```

## Tasks

### 0. [Simple helper function](./0-simple_helper_function.py) :

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

```bash
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
bob@dylan:~$
```

### 1. [Simple pagination](./1-simple_pagination.py) :-

Copy `index_range` from the previous task and the following class into your code

```bash
import csv
import math
from typing import List


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
            pass
```

Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.

- You have to use this [CSV file](./Popular_Baby_Names.csv) (same as the one presented at the top of the project)
- Use `assert` to verify that both arguments are integers greater than 0.
- Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
- If the input arguments are out of range for the dataset, an empty list should be returned.

```bash
bob@dylan:~$  wc -l Popular_Baby_Names.csv 
19419 Popular_Baby_Names.csv
bob@dylan:~$  
bob@dylan:~$ head Popular_Baby_Names.csv
Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
bob@dylan:~$  
bob@dylan:~$  cat 1-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))

bob@dylan:~$ 
bob@dylan:~$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
bob@dylan:~$ 
```

### 2. [Hypermedia pagination](./2-hypermedia_pagination.py) :-

Replicate code from the previous task.

Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:

- `page_size`: the length of the returned dataset page
- `page`: the current page number
- `data`: the dataset page (equivalent to return from previous task)
- `next_page`: number of the next page, `None` if no next page
- `prev_page`: number of the previous page, `None` if no previous page
- `total_pages`: the total number of pages in the dataset as an integer

Make sure to reuse `get_page` in your implementation.

You can use the `math` module if necessary.

```bash
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))

bob@dylan:~$ 
bob@dylan:~$ ./2-main.py
{'page_size': 2, 'page': 1, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2']], 'next_page': 2, 'prev_page': None, 'total_pages': 9709}
---
{'page_size': 2, 'page': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4']], 'next_page': 3, 'prev_page': 1, 'total_pages': 9709}
---
{'page_size': 3, 'page': 100, 'data': [['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Londyn', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Amirah', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'McKenzie', '14', '39']], 'next_page': 101, 'prev_page': 99, 'total_pages': 6473}
---
{'page_size': 0, 'page': 3000, 'data': [], 'next_page': None, 'prev_page': 2999, 'total_pages': 195}
bob@dylan:~$ 
```

### 3. [Deletion-resilient hypermedia pagination](./3-hypermedia_del_pagination.py) :-

The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.

Start `3-hypermedia_del_pagination.py` with this code:

```bash
#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


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
            pass
```

Implement a `get_hyper_index` method with two integer arguments: `index` with a `None` default value and `page_size` with default value of 10.

- The method should return a dictionary with the following key-value pairs:
  - `index`: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with `page_size` 20, and no data was removed from the dataset, the current index should be 60.
  - `next_index`: the next index to query with. That should be the index of the first item after the last item on the current page.
  - `page_size`: the current page size
  - `data`: the actual page of the dataset

#### Requirements/Behavior:-

- Use `assert` to verify that `index` is in a valid range.
- If the user queries index 0, `page_size` 10, they will get rows indexed 0 to 9 included.
- If they request the next index (10) with `page_size` 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.

```bash
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")        


index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get('next_index'), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> the first data retreives is not the same as the first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -> same data page as the request 2-
print(server.get_hyper_index(res.get('next_index'), page_size))

bob@dylan:~$ 
bob@dylan:~$ ./3-main.py
AssertionError raised when out of range
Nb items: 19418
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4']], 'page_size': 2, 'next_index': 5}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
Nb items: 19417
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']], 'page_size': 2, 'next_index': 6}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
bob@dylan:~$ 
```
