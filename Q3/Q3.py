from random import randint
from random import shuffle

# https://github.com/peterhil/leftrb/blob/master/leftrb/bst.py

# !/usr/bin/env python -u
# encoding: utf-8
#
# Leftrb is a Left-Leaning Red-Black tree implementation in Python.
# Copyright (c) 2013, Peter Hillerström <peter.hillerstrom@gmail.com>
#
# This file is part of Leftrb.
#
# Leftrb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
# Leftrb is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Leftrb.  If not, see <http://www.gnu.org/licenses/>.
"""
Binary search tree.
"""


class BinarySearchTree(object):
    """
    Basic unbalanced (inefficient) binary search tree.
    For extending into different balanced binary trees.
    """
    root = None

    class Node(object):
        """
        BST tree node.
        """
        left = right = None

        def __init__(self, key, val=None):
            self.key = key
            self.val = val

        def search(self, key):
            """
            Search the subtree for a key. Return a value or None.
            """
            if self.key == key:
                return self.val if self.val is not None else self.key
            elif key < self.key and self.left:
                return self.left.search(key)
            elif self.key < key and self.right:
                return self.right.search(key)
            return None

        def insert(self, key, value=None):
            """
            Insert a node recursively.
            """
            if self.key == key:
                self.val = value
            elif key < self.key:
                if self.left is None:
                    self.left = self.__class__(key, value)
                else:
                    self.left = self.left.insert(key, value)
            else:
                if self.right is None:
                    self.right = self.__class__(key, value)
                else:
                    self.right = self.right.insert(key, value)
            return self

        def min(self):
            """
            Smallest node in the subtree.
            """
            return self.key if self.left is None else self.left.min()

        def max(self):
            """
            Largest node in the subtree.
            """
            return self.key if self.right is None else self.right.max()

    def search(self, key):
        """
        Search the tree with a key. Return a value or None.
        """
        return self.root.search(key) if self.root is not None else None

    def insert(self, key, value=None):
        """
        Insert a key with optional value into tree.
        """
        self.root = self.Node(key, value) if self.root is None else self.root.insert(key, value)


# https://github.com/peterhil/leftrb/blob/master/leftrb/llrb.py

# !/usr/bin/env python -u
# encoding: utf-8
#
# Leftrb is a Left-Leaning Red-Black tree implementation in Python.
# Copyright (c) 2013, Peter Hillerström <peter.hillerstrom@gmail.com>
#
# This file is part of Leftrb.
#
# Leftrb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
# Leftrb is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Leftrb.  If not, see <http://www.gnu.org/licenses/>.
"""
Leftrb/LLRB is a Left-Leaning Red-Black (LLRB) implementation
of 2–3 balanced binary search trees in Python.
This is a straightforward port of the code in the article
“Left-leaning Red-Black Trees”
http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf
by Robert Sedgewick of Princeton University.
"""

import sys

__all__ = ['LeftRB']

RED = True
BLACK = False


def is_red(h):
    """
    Is the node (h) red?
    """
    return isinstance(h, LeftRB.Node) and h.color == RED


def is_black(h):
    """
    Is the node (h) black?
    """
    return not is_red(h)


class LeftRB(BinarySearchTree, object):
    """
    Left-Leaning Red-Black (LLRB) is an implementation of
    2–3 balanced binary search tree.
    Ported to Python from code and description on
    paper “Left-leaning Red-Black Trees” by Robert Sedgewick:
    http://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf
    """
    root = None

    class Node(BinarySearchTree.Node, object):
        """
        LeftRB tree node.
        """

        def __init__(self, key, val=None):
            super(self.__class__, self).__init__(key, val)
            self.color = RED  # new nodes are always red
            self.height = 1

        def insert(self, key, value=None):
            """
            Recursively insert a node with key and optional value into the tree below.
            """
            # Move this to the end to get 2-3 trees
            if is_red(self.left) and is_red(self.right):
                self._flip_colors()

            self = super(LeftRB.Node, self).insert(key, value)

            if is_red(self.right) and is_black(self.left):
                self = self._rotate_left()
            if is_red(self.left) and self.left and is_red(self.left.left):
                self = self._rotate_right()

            return self._setHeight()

        def size(self):
            """
            Number of nodes in the subtree below node.
            """
            # TODO Cache into self.N
            return 1 + sum(map(lambda child: child.size(), filter(None, [self.left, self.right])))

        def __repr__(self):
            return "<{0} at {1}, key={2}, value={3}, left={6}, right={7}, color={4}, height={5}>".format(
                self.__class__.__name__,
                id(self),
                self.key,
                self.val,
                'red' if is_red(self) else 'black',
                self.height,
                self.left and self.left.key or None,
                self.right and self.right.key or None,
            )

        def _fix_up(self):
            """
            Fix the Left-leaning Red-black tree properties
            with upto two rotations and a possible color flip.
            """
            if is_red(self.right):
                self = self._rotate_left()

            if is_red(self.left) and self.left and is_red(self.left.left):
                self = self._rotate_right()

            if is_red(self.left) and is_red(self.right):
                self._flip_colors()

            return self._setHeight()

        def _flip_colors(self):
            """
            Flip colors to split a 4-node
            """
            self.color = not self.color
            self.left.color = not self.left.color
            self.right.color = not self.right.color

        def _move_red_left(self):
            """
            Assuming that self is red and both self.left and self.left.left
            are black, make self.left or one of its children red.
            """
            self._flip_colors()
            if self.right and is_red(self.right.left):
                self.right = self.right._rotate_right()
                self = self._rotate_left()
                self._flip_colors()
            return self

        def _move_red_right(self):
            """
            Assuming that self is red and both self.right and self.right.left
            are black, make self.right or one of its children red.
            """
            self._flip_colors()
            if self.left and is_red(self.left.left):
                self = self._rotate_right()
                self._flip_colors()
            return self

        def _rotate_left(self):
            """
            Left rotate (right link of self)
                   V         |          V <--left or right, red or black
                   |         |          |
            out<--(x)   <<< LEFT       (s) <--in
                 // \        |         / \\  <--red
               (s)   3       |        1   (x)
               / \           |            / \
              1   2          |           2   3
            """
            x = self.right
            self.right = x.left
            x.left = self
            x.color = self.color
            self.color = RED
            return x

        def _rotate_right(self):
            """
            Right rotate (left link of self)
                   V         |          V <--left or right, red or black
                   |         |          |
            in--> (s)     RIGHT >>>    (x)-->out
                 // \        |         / \\  <--red
               (x)   3       |        1   (s)
               / \           |            / \
              1   2          |           2   3
            """
            x = self.left
            self.left = x.right
            x.right = self
            x.color = self.color
            self.color = RED
            return x

        def _delete(self, key):
            """
            Delete a node with the given key (recursively) from the tree below.
            """
            assert self.search(key) is not None

            if key < self.key:
                if is_black(self.left) and self.left and is_black(self.left.left):
                    self = self._move_red_left()
                self.left = self.left._delete(key)
            else:
                if is_red(self.left):
                    self = self._rotate_right()

                if key == self.key and self.right is None:
                    return None

                if is_black(self.right) and self.right and is_black(self.right.left):
                    self = self._move_red_right()

                if key == self.key:
                    self.value = self.right.search(self.right.min())
                    self.key = self.right.min()
                    self.right = self.right._delete_min()
                else:
                    self.right = self.right._delete(key)

            return self._fix_up()

        def _delete_min(self):
            """
            Delete the smallest node on the (left) subtree below
            while maintaining balance.
            """
            if self.left is None:
                return None

            if is_black(self.left) and self.left and is_black(self.left.left):
                self = self._move_red_left()

            self.left = self.left._delete_min()

            return self._fix_up()

        def _delete_max(self):
            """
            Delete the largest node on the (right) subtree below
            while maintaining balance.
            """
            if is_red(self.left):
                self = self._rotate_right()

            if self.right is None:
                return None

            if is_black(self.right) and self.right and is_black(self.right.left):
                self = self._move_red_right()

            self.right = self.right._delete_max()

            return self._fix_up()

        def _setHeight(self):
            """
            Update height.
            """
            self.height = 1 + max(self.left and self.left.height or 0,
                                  self.right and self.right.height or 0)
            return self

    def is_empty(self):
        """
        Is the tree empty?
        """
        return self.root is None

    def __contains__(self, key):
        """
        Does the tree contain key?
        """
        return self.search(key) is not None

    def __len__(self):
        """
        Number of nodes in the tree.
        """
        return 0 if self.root is None else self.root.size()

    def height(self):
        """
        Height of the tree.
        """
        return 0 if self.root is None else self.root.height

    def min(self):
        """
        Smallest node in the tree.
        """
        return None if self.root is None else self.root.min()

    def max(self):
        """
        Largest node in the tree.
        """
        return None if self.root is None else self.root.max()

    def insert(self, key, value=None):
        """
        Insert a key with optional value into the tree.
        """
        super(LeftRB, self).insert(key, value)
        self.root.color = BLACK

    def delete(self, key):
        """
        Delete a node with the given key from the tree.
        """
        if key not in self:
            sys.stderr.write("Tree does not contain key '{0}'.\n".format(key))
            return False

        if is_black(self.root.left) and is_black(self.root.right):
            self.root.color = RED

        if self.root is not None:
            self.root = self.root._delete(key)

        if not self.is_empty():
            self.root.color = BLACK

    def delete_min(self):
        """
        Delete the smallest node while maintaining balance.
        """
        self.root = self.root._delete_min()
        self.root.color = BLACK

    def delete_max(self):
        """
        Delete the largest node while maintaining balance.
        """
        self.root = self.root._delete_max()
        self.root.color = BLACK


del BinarySearchTree


def inorder_traverse(nood):
    red_count = 0
    if not nood.left or not nood.right:
        if is_red(nood):
            return 1
        else:
            return 0

    red_count += inorder_traverse(nood.left)
    if is_red(nood):
        red_count += 1
    red_count += inorder_traverse(nood.right)

    return red_count


def red_percentage(llrb):
    red_count = inorder_traverse(llrb.root)
    total_count = llrb.__len__()
    return red_count / total_count


def q3_experiment():
    num_trials = 100
    for N in [10000, 100000, 1000000]:
        results = []
        for _ in range(num_trials):
            shuffled_inserts = [randint(1, N) for _ in range(N)]
            llrb = LeftRB()
            for insert in shuffled_inserts:
                llrb.insert(insert)
            results.append(red_percentage(llrb))
        print("Average red node percentage after {} trials is {:.2f}% for {} random nodes".format(num_trials, 100*sum(results)/len(results),N))


def main():
    print("Running only 1 trial and 10^4 and 10^5 so you don't have to wait")
    num_trials = 1
    for N in [10000, 100000]:  # , 1000000]:
        results = []
        for _ in range(num_trials):
            shuffled_inserts = [randint(1, N) for _ in range(N)]
            llrb = LeftRB()
            for insert in shuffled_inserts:
                llrb.insert(insert)
            results.append(red_percentage(llrb))
        print("Average red node percentage after {} trials is {:.2f}% for {} random nodes".format(num_trials,
                                                                                              100 * sum(results) / len(
                                                                                                  results), N))


if __name__ == '__main__':
    main()
