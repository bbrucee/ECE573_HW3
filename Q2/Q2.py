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


# https://stackoverflow.com/questions/36242046/internal-path-length-of-red-black-tree

def internal_path_length(root_node, curr_depth=0):
    """
    Computes internal path length
    """
    if not root_node:
        return 0
    else:
        return curr_depth + internal_path_length(root_node.left, curr_depth + 1) + internal_path_length(root_node.right,
                                                                                                        curr_depth + 1)


def q2_experiment():
    num_trials = 100
    shuffle_results = []
    sorted_results = []
    for N in range(10, 1000, 10):
        shuffle_mean = []
        sorted_mean = []
        for _ in range(num_trials):
            shuffled_inserts = list(range(N))
            sorted_inserts = shuffled_inserts.copy()
            shuffle(shuffled_inserts)

            shuffle_experiment = BinarySearchTree()
            sorted_experiment = BinarySearchTree()

            for insert in shuffled_inserts:
                shuffle_experiment.insert(insert, insert)
            for insert in sorted_inserts:
                sorted_experiment.insert(insert, insert)

            shuffle_internal_path_length = internal_path_length(shuffle_experiment.root)
            shuffle_mean.append(shuffle_internal_path_length / N)

            sorted_internal_path_length = internal_path_length(sorted_experiment.root)
            sorted_mean.append(sorted_internal_path_length / N)
        print("After {} trials, the average path length for {} random insertions is {}".format(num_trials, N,
                                                                                               sum(shuffle_mean) / len(
                                                                                                   shuffle_mean)))
        print("After {} trials, the average path length for {} sorted insertions is {}".format(num_trials, N,
                                                                                               sum(sorted_mean) / len(
                                                                                                   sorted_mean)))

        shuffle_results.append(sum(shuffle_mean) / len(shuffle_mean))
        sorted_results.append(sum(sorted_mean) / len(sorted_mean))



def main():
    num_trials = 100
    shuffle_results = []
    sorted_results = []
    for N in range(10, 250, 10):
        shuffle_mean = []
        sorted_mean = []
        for _ in range(num_trials):
            shuffled_inserts = list(range(N))
            sorted_inserts = shuffled_inserts.copy()
            shuffle(shuffled_inserts)

            shuffle_experiment = BinarySearchTree()
            sorted_experiment = BinarySearchTree()

            for insert in shuffled_inserts:
                shuffle_experiment.insert(insert, insert)
            for insert in sorted_inserts:
                sorted_experiment.insert(insert, insert)

            shuffle_internal_path_length = internal_path_length(shuffle_experiment.root)
            shuffle_mean.append(shuffle_internal_path_length / N)

            sorted_internal_path_length = internal_path_length(sorted_experiment.root)
            sorted_mean.append(sorted_internal_path_length / N)
        print("After {} trials, the average path length for {} random insertions is {}".format(num_trials, N,
                                                                                               sum(shuffle_mean) / len(
                                                                                                   shuffle_mean)))
        print("After {} trials, the average path length for {} sorted insertions is {}".format(num_trials, N,
                                                                                               sum(sorted_mean) / len(
                                                                                                   sorted_mean)))

        shuffle_results.append(sum(shuffle_mean) / len(shuffle_mean))
        sorted_results.append(sum(sorted_mean) / len(sorted_mean))


if __name__ == '__main__':
    main()
