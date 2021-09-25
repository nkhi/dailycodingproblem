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

# Tree Node def'n
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Helpers
def printPaths(root):
    "Start recursively printing paths"
    
    path = []
    printPathsRec(root, path, 0)

def printPathsRec(root, path, pathLen):

    # stopping cond for leaves
	if root is None:
		return

    # keep track of pathlen
	if(len(path) > pathLen):
		path[pathLen] = root.data
	else:
		path.append(root.data)
	pathLen = pathLen + 1

    # print final path if you're at a leaf
    # otherwise print the paths of the children
	if root.left is None and root.right is None:
		print(f"PATH: {path[0:pathLen]}")
	else:
		printPathsRec(root.left, path, pathLen)
		printPathsRec(root.right, path, pathLen)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
printPaths(root)