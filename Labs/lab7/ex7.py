"""
BTNode exercises
"""
from typing import Union, Any


class BTNode:
    """Binary Tree node.

    data - data this node represents
    left - left child
    right - right child
    """
    data: object
    left: Union["BTNode", None]
    right: Union["BTNode", None]

    def __init__(self, data: object,
                 left: Union["BTNode", None] = None,
                 right: Union["BTNode", None] = None) -> None:
        """
        Create BTNode (self) with data and children left and right.

        An empty BTNode is represented by None.

        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other: Any) -> bool:
        """
        Return whether BTNode (self) is equivalent to other.

        >>> BTNode(7).__eq__('seven')
        False
        >>> b1 = BTNode(7, BTNode(5))
        >>> b1.__eq__(BTNode(7, BTNode(5), None))
        True
        """
        return (type(self) == type(other) and
                self.data == other.data and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self) -> str:
        """
        Represent BTNode (self) as a string that can be evaluated to
        produce an equivalent BTNode.

        >>> BTNode(1, BTNode(2), BTNode(3))
        BTNode(1, BTNode(2, None, None), BTNode(3, None, None))
        """
        return 'BTNode({}, {}, {})'.format(self.data,
                                           repr(self.left),
                                           repr(self.right))

    def __str__(self, indent: str = "") -> str:
        """
        Return a user-friendly string representing BTNode (self) inorder.
        Indent by indent.

        >>> b = BTNode(1, BTNode(2, BTNode(3)), BTNode(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = self.right.__str__(indent + '    ') if self.right else ''
        left_tree = self.left.__str__(indent + '    ') if self.left else ''
        return right_tree + '{}{}\n'.format(indent, str(self.data)) + left_tree


def list_longest_path(node: Union[BTNode, None]) -> list:
    """ List the data in a longest path of node.

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BTNode(5))
    [5]
    >>> b1 = BTNode(7)
    >>> b2 = BTNode(3, BTNode(2), None)
    >>> b3 = BTNode(5, b2, b1)
    >>> list_longest_path(b3)
    [5, 3, 2]
    """
    if not node:
        return []
    else:
        if len(list_longest_path(node.left)) >= len(list_longest_path(node.right)):
            return [node.data] + list_longest_path(node.left)
        return [node.data] + list_longest_path(node.right)


def list_between(node: Union[BTNode, None], start: object, end: object) -> list:
    """
    Return a Python list of all data in the binary search tree
    rooted at node that are between start and end (inclusive).

    A binary search tree t is a BTNode where all nodes in the subtree
    rooted at t.left are less than t.data, and all nodes in the subtree
    rooted at t.right are more than t.data

    Avoid visiting nodes with values less than start or greater than end.

    >>> b_left = BTNode(4, BTNode(2), BTNode(6))
    >>> b_right = BTNode(12, BTNode(10), BTNode(14))
    >>> b = BTNode(8, b_left, b_right)
    >>> list_between(None, 3, 13)
    []
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    """
    if not node:
        return []
    if start > node.data:
        return list_between(node.right, start, end)
    if end < node.data:
        return list_between(node.left, start, end)
    else:
        return list_between(node.left, start, end) + [node.data]\
               + list_between(node.right, start, end)


def list_even_between(t, start, stop):
    """"(BTNode, int, int) -> list
    Return a list of data in the tree rooted at t that
    (a) are even and (b) are between start and stop, inclusive.
    Assume that t is the root of a (possibly empty) binary
    search tree with integer elements. That is, assume:
        -- every non-empty node has integer data
        -- all data in any left sub-tree is less than the
           data in the root node
        -- all data in any right sub-tree is more than the
           data in the root node.
    >>> t = None
    >>> list_even_between(t, 5, 9)
    []
    >>> t1 = BTNode(4, BTNode(2), BTNode(5))
    >>> t2 = BTNode(9, BTNode(8), BTNode(10))
    >>> t3 = BTNode(7, t1, t2)
    >>> L = list_even_between(t3, 3, 8)
    >>> L.sort()
    >>> L
    [4, 8]
    """
    if not t:
        return []
    else:
        if start > t.data:
            return list_even_between(t.right, start, stop)
        if stop < t.data:
            return list_even_between(t.left, start, stop)
        else:
            acc = []
            if t.data % 2 == 0:
                acc.append(t.data)
            return list_even_between(t.left, start, stop) + acc +\
                   list_even_between(t.right, start, stop)


def count_shallower(t: Union[BTNode, None], n: int) -> int:
    """ Return the number of nodes in tree rooted at t with
    depth less than n.

    >>> t = BTNode(0, BTNode(1, BTNode(2)), BTNode(3))
    >>> count_shallower(t, 2)
    3
    """
    if not t:
        return 0
    if n == 0:
        return 0
    else:
        acc = 1
        for c in [t.left, t.right]:
            acc += count_shallower(c, n - 1)
        return acc


def concatenate_leaves(t: Union[BTNode, None]) -> str:
    """
    Return the string values in the Tree rooted at t concatenated from left to right.
    Assume all leaves have string value.

    >>> t1 = BTNode("one")
    >>> t2 = BTNode("two")
    >>> t3 = BTNode("three", t1, t2)
    >>> concatenate_leaves(t1)
    'one'
    >>> concatenate_leaves(t3)
    'onetwo'
    """
    if not t:
        return ''
    else:
        if not (t.left and t.right):
            return t.data
        else:
            return concatenate_leaves(t.left) + concatenate_leaves(t.right)


def count_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the number of leaves in BinaryTree t.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> count_leaves(None)
    0
    >>> count_leaves(t3)
    2
    """
    if not t:
        return 0
    else:
        if not (t.left and t.right):
            return 1
        return count_leaves(t.left) + count_leaves(t.right)


def sum_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the leaves of BinaryTree t.  Return
    0 if t is empty.
    Assume all leaves have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_leaves(t2)
    2
    >>> sum_leaves(t3)
    3
    """
    if not t:
        return 0
    else:
        if not (t.left and t.right):
            return t.data
        else:
            return sum_leaves(t.left) + sum_leaves(t.right)


def sum_internal(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the internal nodes of BinaryTree t.  Return
    0 if t is empty.
    Assume all internal nodes have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_internal(t2)
    0
    >>> sum_internal(t3)
    3
    """
    if not t:
        return 0
    else:
        if not (t.left and t.right):
            return 0
        else:
            return t.data + sum_internal(t.left) + sum_internal(t.right)


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config='pylint.txt')
    import doctest

    doctest.testmod()
