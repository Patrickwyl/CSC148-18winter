""" recursion exercises with nested lists
"""
from typing import List, Union


def gather_lists(list_: List[List[object]]) -> List[object]:
    """
    Return the concatenation of the sublists of list_.

    >>> list_ = [[1, 2], [3, 4]]
    >>> gather_lists(list_)
    [1, 2, 3, 4]
    """
    # special form of sum for "adding" lists
    return sum(list_, [])


def list_all(obj: Union[list, object]) -> list:
    """
    Return a list of all non-list elements in obj or obj's sublists, if obj
    is a list.  Otherwise, return a list containing obj.

    >>> obj = 17
    >>> list_all(obj)
    [17]
    >>> obj = [1, 2, 3, 4]
    >>> list_all(obj)
    [1, 2, 3, 4]
    >>> obj = [[1, 2, [3, 4], 5], 6]
    >>> all([x in list_all(obj) for x in [1, 2, 3, 4, 5, 6]])
    True
    >>> all ([x in [1, 2, 3, 4, 5, 6] for x in list_all(obj)])
    True
    """
    if not isinstance(obj, list):
        return [obj]
    else:
        return sum([list_all(i) for i in obj], [])


def max_length(obj: Union[list, object]) -> int:
    """
    Return the maximum length of obj or any of its sublists, if obj is a list.
    otherwise return 0.

    >>> max_length(17)
    0
    >>> max_length([1, 2, 3, 17])
    4
    >>> max_length([[1, 2, 3, 3], 4, [4, 5]])
    4
    """
    if not isinstance(obj, list):
        return 0
    else:
        for i in obj:
            if isinstance(i, list):
                return max(max_length(i) for i in obj)
            return len(obj)


def list_over(obj: Union[list, str], n: int) -> List[str]:
    """
    Return a list of strings of length greater than n in obj,
    or sublists of obj, if obj is a list.
    If obj is a string of length greater than n, return a list
    containing obj.  Otherwise return an empty list.

    >>> list_over("five", 3)
    ['five']
    >>> list_over("five", 4)
    []
    >>> list_over(["one", "two", "three", "four"], 3)
    ['three', 'four']
    """
    if not isinstance(obj, list):
        if len(obj) > n:
            return [obj]
        return []
    else:
        return sum([list_over(i, n) for i in obj], [])


def list_even(obj: Union[list, int]) -> List[int]:
    """
    Return a list of all even integers in obj,
    or sublists of obj, if obj is a list.  If obj is an even
    integer, return a list containing obj.  Otherwise return
    en empty list.

    >>> list_even(3)
    []
    >>> list_even(16)
    [16]
    >>> list_even([1, 2, 3, 4, 5])
    [2, 4]
    >>> list_even([1, 2, [3, 4], 5])
    [2, 4]
    >>> list_even([1, [2, [3, 4]], 5])
    [2, 4]
    """
    if not isinstance(obj, list):
        if obj % 2 == 0:
            return [obj]
        return []
    else:
        return sum([list_even(i) for i in obj], [])


def count_even(obj: Union[list, int]) -> int:
    """
    Return the number of even numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 1
    if it is an even number and 0 if it is an odd number.

    >>> count_even(3)
    0
    >>> count_even(16)
    1
    >>> count_even([1, 2, [3, 4], 5])
    2
    """
    if isinstance(obj, int):
        if obj % 2 == 0:
            return 1
        return 0
    else:
        return sum(count_even(i) for i in obj)


def count_all(obj: Union[list, object]) -> int:
    """
    Return the number of elements in obj or sublists of obj if obj is a list.
    Otherwise, if obj is a non-list return 1.

    >>> count_all(17)
    1
    >>> count_all([17, 17, 5])
    3
    >>> count_all([17, [17, 5], 3])
    4
    """
    if not isinstance(obj, list):
        return 1
    else:
        return sum(count_all(i) for i in obj)


def count_above(obj: Union[list, int], n: int) -> int:
    """
    Return tally of numbers in obj, and sublists of obj, that are over n, if
    obj is a list.  Otherwise, if obj is a number over n, return 1.  Otherwise
    return 0.

    >>> count_above(17, 19)
    0
    >>> count_above(19, 17)
    1
    >>> count_above([17, 18, 19, 20], 18)
    2
    >>> count_above([17, 18, [19, 20]], 18)
    2
    """
    if isinstance(obj, int):
        if obj > n:
            return 1
        return 0
    else:
        return sum(count_above(i, n) for i in obj)


def contains_satisfier(list_, predicate):
    """
    Return whether possibly-nested list_ contains a non-list element
    that satisfies (returns True for) predicate.
    @param list list_: list to check for predicate satisfiers
    @param (object)->bool predicate: boolean function
    @rtype: bool
    >>> list_ = [5, [6, [7, 8]], 3]
    >>> def p(n): return n > 7
    >>> contains_satisfier(list_, p)
    True
    >>> def p(n): return n > 10
    >>> contains_satisfier(list_, p)
    False
    """
    if not isinstance(list_, list):
        return predicate(list_)
    else:
        for sublist in list_:
            if contains_satisfier(sublist, predicate):
                return True
        return False


def list_level(obj: Union[list, int], d: int) -> list:
    """
    Return a list of items at the depth of d in obj.
    >>> list_level([17, 18, [19, 20], 12], 2)
    [19, 20]
    >>> list_level([17, 18, [19, 20], 12], 1)
    [17, 18, 12]
    """
    if d == 0:
        if not isinstance(obj, list):
            return [obj]
        else:
            return []
    else:
        if not isinstance(obj, list):
            return []
        else:
            acc = []
            for sublist in obj:
                acc.extend(list_level(sublist, d - 1))
        return acc
