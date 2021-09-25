# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a binary tree, return all paths from the root to leaves.

# For example, given the tree:

#    1
#   / \
#  2   3
#     / \
#    4   5

# Return [[1, 2], [1, 3, 4], [1, 3, 5]].

# always good to have some tree practice

class TreeNode(data, left=None, right=None):

    def __init__(self, data, left, right):
        "Make a new TreeNode"

        self.data = data
        self.left = left
        self.right = right

    def setLeft(self, left: TreeNode):
        self.left = left

    def setRight(self, right: TreeNode):
        self.left = right

    def walk(self):
        "Walk down the rest of the tree from self"

        print(self.data)
        walk(self.left) if self.left is not None else \
        walk(self.right) if self.right is not None else \
        print("\n")