import unittest
import random
from hypothesis import given
from hypothesis import note
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from hypothesis.strategies import recursive
from ex6 import count_leaves


def make_children_list(children):
    """
    Return a list of child Trees generated by children.

    @param list[object]|object children: The children values and trees
    @rtype: (list[Tree], int)
    """
    num_leaves = 0
    if type(children) != list:
        return ([Tree(children)], 1)

    ret_children = []
    for child in children:
        rec_call = make_children_list(child)

        if type(child) == list:
            ret_children.append(Tree(random.randint(0, 100), rec_call[0]))
            if not rec_call[0]:
                num_leaves += 1
        else:
            ret_children += rec_call[0]

        num_leaves += rec_call[1]

    # Pick a random value for the Tree's value
    return (ret_children, num_leaves)

class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """
    def __init__(self, value=None, children=None):
        """
        Create Tree self with content value and 0 or more children

        @param Tree self: this tree
        @param object value: value contained in this tree
        @param list[object|None] children: possibly-empty list of children
        @rtype: None
        """
        self.value = value
        # copy children if not None
        self.children = children.copy() if children else []

    def __repr__(self):
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        @param Tree self: this tree
        @rtype: str

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

class CountInternalTests(unittest.TestCase):
    def test_returns_int(self):
        """
        Test count_leaves to make sure it returns an int.
        """
        return_type = type(count_leaves(Tree(0, [Tree(1, [Tree(2)])])))
        self.assertEqual(return_type, int, "count_leaves should return type" +
                         "int, but instead returned type {}.".format(return_type
                                                                     ))

    def test_leaf_node(self):
        """
        Test count_leaves on a leaf node.
        """
        self.assertEqual(count_leaves(Tree(0)), 1, "Leaf nodes should " +
                         "have 1 leaf node.")

    def test_one_leaf_child(self):
        """
        Test count_leaves on a tree containing only a root and its leaf child.
        """
        t = Tree(0, [Tree(1)])

        self.assertEqual(count_leaves(t), 1, "Only leaf nodes should be " +
                         "included in the count and not nodes with children.")

    def test_multiple_leaf_children(self):
        """
        Test count_leaves on a tree containing only a root and its children
        which are all leaves.
        """
        t = Tree(0, [Tree(1), Tree(2)])

        self.assertEqual(count_leaves(t), 2, "Leaf nodes should be " +
                         "included in the count, while root nodes (with " +
                         "children) should not.")

    def test_multiple_non_leaf_children(self):
        """
        Test count_leaves on a tree containing only a root and its children
        which are all subtrees with children.
        """
        t = Tree(0, [Tree(1, [Tree(3), Tree(5)]), Tree(2, [Tree(4), Tree(6)])])

        self.assertEqual(count_leaves(t), 4, "All nodes with no children " +
                         "should be counted as leaf nodes.")

    @given(integers(min_value = -99, max_value = 99),
           recursive(integers(min_value = -99, max_value = 99), lists,
                     max_leaves = 20))
    def test_count_internal(self, value, children):
        """
        Test the correctness of count_leaves against the solution.
        """
        (children_list, num_leaves) = make_children_list(children)
        t = Tree(value, children_list)

        if not children_list:
            num_leaves += 1

        actual = count_leaves(t)
        self.assertEqual(actual, num_leaves,
                         ("count_leaves on the Tree\n{}\nReturned {}" +
                          " instead of {}.").format(t.__repr__(), actual,
                                                   num_leaves))

if __name__ == "__main__":
    unittest.main()
