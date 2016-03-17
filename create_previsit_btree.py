#!/usr/bin/env python
# coding=utf-8


class TreeNode(object):

    def __init__(self):
        self.data = '#'
        self.left = None
        self.right = None


class Tree(TreeNode):

    def create_tree(self, tree):
        date = raw_input()
        if date == '#':
            tree = None
        else:
            tree.data = date
            tree.left = TreeNode()
            self.create_tree(tree.left)
            tree.right = TreeNode()
            self.create_tree(tree.right)

    def visit(self, tree):
        if tree.data is not '#':
            print str(tree.data)

    def pre_order(self, tree):
        if tree is not None:
            self.visit(tree)
            self.pre_order(tree.left)
            self.pre_order(tree.right)
tree = TreeNode()
bt = Tree()
bt.create_tree(tree)
bt.pre_order(tree)
