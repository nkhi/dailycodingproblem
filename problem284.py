# Good morning! Here's your coding interview problem for today.

# This problem was asked by Yext.

# Two nodes in a binary tree can be called cousins if they are on 
# the same level of the tree but have different parents. 
# For example, in the following diagram 4 and 6 are cousins.

#     1
#    / \
#   2   3
#  / \   \
# 4   5   6

# Given a binary tree and a particular node, find all cousins of that node.

# interpretation: need to find the depth of the given node in the given BTree, and then 
#                 return the number of nodes at that depth - 1

# A binary tree node
class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = Node(l) if l else None
        self.r = Node(r) if r else None

    def l_val(self):
        return None if self.l is None else self.l.val

    def r_val(self):
        return None if self.r is None else self.r.val

    def parent_of(self, node: int):
        return node in [self.l_val(), self.r_val()]

    def __str__(self):
        return str(self.val)

def level(r: Node, value: int, lev=0) -> int:
    "Return the depth of the BTree Node 'r'. "
    if r is None:
        return 0
    elif r.val == value:
        return lev + 1
    left_lev = level(r.l, value, lev + 1)
    if left_lev > 0:
        return left_lev
    return level(r.r, value, lev + 1)

def cousin_finder(r: Node, node: int, lev: int) -> list:
    "Return a list of cousins of the BTree Node 'r'. Used in cousins."
    if r is None:
        return []
    elif lev == 2 and r.parent_of(node):
        return []
    elif lev == 1:
        return [r.val]

    res = []
    res += cousin_finder(r.l, node, lev - 1)
    res += cousin_finder(r.r, node, lev - 1)
    return res

def cousins(r: Node, node: int) -> list:
    "Returns the entire set of cousins of a given BTree Node 'r'."
    lev = level(r, node)
    return cousin_finder(r, node, lev)

if __name__ == "__main__":
    # establish given example as a tree with extra cousin 7
    root = Node(1, 2, 3)
    root.l.l = Node(4)
    root.l.r = Node(5)
    root.r.l = Node(6)
    root.r.r = Node(7)

    # verify level works
    assert level(root, 1) == 1
    assert level(root, 2) == 2
    assert level(root, 3) == 2
    assert level(root, 4) == 3
    assert level(root, 5) == 3
    assert level(root, 6) == 3
    assert level(root, 7) == 3
    assert level(root, 10) == 0

    # calculate cousin
    c = cousins(root, 5)
    assert c == [6, 7], c
