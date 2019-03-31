import os


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


# rank in O(n) with inorder traversal
def inorder(node, key_queue):
    if not node:
        return -1
    inorder(node.left, key_queue)
    key_queue.append(node.key)
    inorder(node.right, key_queue)


def rank(root, key):
    q = []
    inorder(root, q)
    return q.index(key)


def select(root, key):
    q = []
    inorder(root, q)
    return q[key]


def main():
    try:
        # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
        rel_path = "/data/select-data.txt"
        cwd = os.getcwd()
        abs_file_path = cwd + rel_path
        input_file = open(abs_file_path)
        data_array = []
        print("Loading data from {}".format(abs_file_path))
        for line in input_file.readlines():
            data_array.append(int(line))
        input_file.close()
        print("Adding data to a Binary Search Tree")
        tree = BinarySearchTree()
        for node in data_array:
            tree.insert(node, node)
        print("Result from select(7) is {}".format(select(tree.root, 7)))
        print("Result from rank(7) is {}".format(rank(tree.root, 7)))

    except IndexError:
        print("No input data file")


if __name__ == '__main__':
    main()
