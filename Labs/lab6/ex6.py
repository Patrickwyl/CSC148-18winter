""" Tree class and functions.
"""
from csc148_queue import Queue
from typing import Any, Callable, List


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        # copy children if not None
        self.children = children[:] if children is not None else []

    def __repr__(self) -> str:
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('Tree({}, {})'.format(repr(self.value), repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other: Any) -> bool:
        """
        Return whether this Tree is equivalent to other.
        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent=0) -> str:
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual clue.

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        """
        root_str = indent * " " + str(self.value)
        return '\n'.join([root_str] +
                         [c.__str__(indent + 3) for c in self.children])


def list_internal(t: Tree) -> list:
    """
    Return list of values in internal nodes of t.

    >>> t = Tree(0)
    >>> list_internal(t)
    []
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_internal(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    """
    if not t.children:
        return []
    else:
        acc = [t.value]
        for subtree in t.children:
            acc.extend(list_internal(subtree))
        return acc


def count_internal(t: Tree) -> int:
    """
    Return number of internal nodes of t.

    >>> t = Tree(0)
    >>> count_internal(t)
    0
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> count_internal(t)
    3
    """
    if not t.children:
        return 0
    else:
        acc = 1
        for subtree in t.children:
            acc += count_internal(subtree)
        return acc


def count_leaves(t: Tree) -> int:
    """
    Return the number of leaves in Tree t.

    >>> t = Tree(7)
    >>> count_leaves(t)
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> count_leaves(t)
    6
    """
    if not t.children:
        return 1
    else:
        acc = 0
        for subtree in t.children:
            acc += count_leaves(subtree)
        return acc


def sum_internal(t: Tree) -> int:
    """
    Return sum of the internal (non-leaf) nodes of t.

    Assume all nodes have integer values.

    >>> t = Tree(0)
    >>> sum_internal(t)
    0
    >>> t = descendants_from_list(Tree(1), [2, 3, 4, 5, 6, 7, 8, 9], 3)
    >>> sum_internal(t)
    6
    """
    if not t.children:
        return 0
    else:
        acc = t.value
        for subtree in t.children:
            acc += sum_internal(subtree)
        return acc


def sum_leaves(t: Tree) -> int:
    """
    Return sum of the leaves of t.
    >>> t = Tree(0)
    >>> sum_leaves(t)
    0
    >>> t = descendants_from_list(Tree(1), [2, 3, 4, 5, 6, 7, 8, 9], 3)
    >>> sum_leaves(t)
    39
    """
    if not t.children:
        return t.value
    else:
        acc = 0
        for subtree in t.children:
            acc += sum_leaves(subtree)
        return acc


def arity(t: Tree) -> int:
    """
    Return the maximum branching factor (arity) of Tree t.

    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    4
    """
    if not t.children:
        return 0
    else:
        acc = []
        temp = 0
        for subtree in t.children:
            temp += 1
            acc.append(temp)
            acc.append(arity(subtree))
        return max(acc)


def contains_test_passer(t: Tree, test: Callable[[Any], bool]) -> bool:
    """
    Return whether t contains a value that test(value) returns True for.

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4.5, 5, 6, 7.5, 8.5], 4)
    >>> def greater_than_nine(n): return n > 9
    >>> contains_test_passer(t, greater_than_nine)
    False
    >>> def even(n): return n % 2 == 0
    >>> contains_test_passer(t, even)
    True
    """
    if not t.children:
        return test(t.value)
    else:
        for subtree in t.children:
            if contains_test_passer(subtree, test):
                return True
        return False


def list_if(t: Tree, p: Callable[[Any], bool]) -> list:
    """
    Return a list of values in Tree t that satisfy predicate p(value).

    Assume p is defined on all of t's values.

    >>> def p(v): return v > 4
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_if(t, p)
    >>> set(list_) == {5, 6, 7, 8}
    True
    >>> def p(v): return v % 2 == 0
    >>> list_ = list_if(t, p)
    >>> set(list_)
    {0, 2, 4, 6, 8}
    """
    if not t.children:
        if p(t.value):
            return [t.value]
        return []
    else:
        if p(t.value):
            acc = [t.value]
        else:
            acc = []
        for subtree in t.children:
            acc.extend(list_if(subtree, p))
        return acc


def height(t: Tree) -> int:
    """
    Return the height of the tree.
    >>> t = Tree(13)
    >>> height(t)
    1
    >>> t = descendants_from_list(Tree(13), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> height(t)
    3
    """
    if not t.children:
        return 1
    else:
        acc = []
        for subtree in t.children:
            acc.append(height(subtree))
        return max(acc) + 1


def count_at_depth(t, d):
    """ Return the number of nodes at depth d of t.
    @param Tree t: tree to explore --- cannot be None
    @param int d: depth to report from, non-negative
    @rtype: int
    >>> t = Tree(17, [Tree(0), Tree(1, [Tree(4)]), Tree(2, [Tree(5)]), Tree(3)])
    >>> print(t)
    17
       0
       1
          4
       2
          5
       3

    >>> count_at_depth(t, 0)
    1
    >>> count_at_depth(t, 1)
    4
    >>> count_at_depth(t, 2)
    2
    >>> count_at_depth(t, 5)
    0
    """
    if d < 0:
        return 0
    if d == 0:
        return 1
    else:
        acc = 0
        for subtree in t.children:
            acc += count_at_depth(subtree, d - 1)
        return acc


def level_at_depth(t, d):
    """ Return a list of values of nodes at depth d of t.
    @param Tree t: tree to explore --- cannot be None
    @param int d: depth to report from, non-negative
    @rtype: list
    >>> t = Tree(17, [Tree(0), Tree(1, [Tree(4)]), Tree(2, [Tree(5)]), Tree(3)])
    >>> print(t)
    17
       0
       1
          4
       2
          5
       3

    >>> level_at_depth(t, 0)
    [17]
    >>> level_at_depth(t, 1)
    [0, 1, 2, 3]
    >>> level_at_depth(t, 2)
    [4, 5]
    >>> level_at_depth(t, 5)
    []
    """
    acc = []
    if d < 0:
        return []
    if d == 0:
        acc.append(t.value)
    if t.children:
        for subtree in t.children:
            acc += level_at_depth(subtree, d - 1)
    return acc


def count_odd_above(t, n):
    """
    Return the number of nodes with depth less than n that have odd values.
    Assume t’s nodes have integer values.
    @param Tree t: tree to list values from
    @param int n: depth above which to list values
    @rtype: int
    >>> t1 = Tree(4)
    >>> t2 = Tree(3)
    >>> t3 = Tree(5, [t1, t2])
    >>> count_odd_above(t3, 1)
    1
    """
    if not t.children:
        if n == 0:
            return 0
        elif n == 1:
            if t.value % 2 == 1:
                return 1
            return 0
    else:
        acc = 0
        if t.value % 2 == 1:
            acc += 1
        for subtree in t.children:
            acc += count_odd_above(subtree, n - 1)
        return acc


def list_even_below(t, n):
    """
    Return a list of even values in t with depth greater than n.
    Assume any values in t are integers.
    @param Tree t: tree to list values from
    @param int n: depth below which to list values
    @rtype: list[int]
    >>> t1 = Tree(5)
    >>> t2 = Tree(4)
    >>> t3 = Tree(2, [t1, t2])
    >>> list_even_below(t3, 0)
    [4]
    """
    if not t.children:
        if n < 0:
            if t.value % 2 == 0:
                return [t.value]
        return []
    else:
        acc = []
        for subtree in t.children:
            acc.extend(list_even_below(subtree, n - 1))
        return acc


# helper function that may be useful in the functions
# above
def gather_lists(list_: List[list]) -> list:
    """
    Concatenate all the sublists of L and return the result.

    >>> gather_lists([[1, 2], [3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> gather_lists([[6, 7], [8], [9, 10, 11]])
    [6, 7, 8, 9, 10, 11]
    """
    new_list = []
    for l in list_:
        new_list += l
    return new_list
    # equivalent to...
    # return sum([list_ for list_ in list_], [])


# helpful helper function
def descendants_from_list(t: Tree, list_: list, branching: int) -> Tree:
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        new_t: Tree
        for _ in range(0, branching):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
    import doctest
    doctest.testmod()
