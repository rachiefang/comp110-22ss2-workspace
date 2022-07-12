"""list Utility Funcions."""
__author__ = "730468022"


def only_evens(list1: list[int]) -> list[int]:
    """Returns even numbers given a list."""
    index: int = 0
    for item in list1:
        if item % 2 != 0:
            list1.pop(index)
        index = index + 1
    return list1
    print(list1)


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists, see if they match."""
    if list1 == list2:
        return True
        print(True)
    if list1 != list2:
        return False 
        print(False)


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Given a list and 2 indices, create a subset between them."""
    end: int - 1
    if len(a_list) == start:
        return []
        print([])
    if len(a_list) == 0:
        return []
        print([])
    if start > len(a_list):
        return []
        print([])
    if end <= 0:
        return []
        print([])
    for item in a_list:
        if a_list.index(item) < start:
            a_list.pop(item)
        if a_list.index(item) > end:
            a_list.pop(item)
        if start < 0:
            return a_list[0]
        if end > len(a_list):
            return a_list[len(a_list) - 1]   
    return a_list
    print(a_list)        