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
class BTNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
    
    def PrintTree(self):
        print(self.data)

listOfLists = []

def levelTraversal(root, level):
    if root is None:
        return

    if level >= len(listOfLists):
        list = []
        listOfLists.append(list)
    listOfLists[level].append(root.data)
    levelTraversal(root.left, level+1)
    levelTraversal(root.right, level+1)

def isSibling(root, a , b): 
    if root is None: 
        return 0
  
    return ((root.left == a and root.right ==b) or 
            (root.left == b and root.right == a)or
            isSibling(root.left, a, b) or
            isSibling(root.right, a, b)) 
  
# Recursive function to find level of Node 'ptr' in  
# a binary tree 
def level(root, ptr, lev): 
    if root is None : 
        return 0 
    if root == ptr:  
        return lev 
  
    # Return level if Node is present in left subtree 
    l = level(root.left, ptr, lev+1) 
    if l != 0: 
        return l 
  
    # Else search in right subtree 
    return level(root.right, ptr, lev+1) 
    
# Returns 1 if a and b are cousins, otherwise 0 
def isCousin(root,a, b): 
      
    # 1. The two nodes should be on the same level in  
    # the binary tree 
    # The two nodes should not be siblings(means that  
    # they should not have the smae parent node 
  
    if ((level(root,a,1) == level(root, b, 1)) and 
            not (isSibling(root, a, b))): 
        return 1
    else: 
        return 0 

if __name__ == "__main__":
    root = BTNode(1) 
    root.left = BTNode(2) 
    root.right = BTNode(3) 

    root.left.left = BTNode(4) 
    root.left.right = BTNode(5) 
    root.left.right.right = BTNode(15)
    
    root.right.left = BTNode(6) 
    root.right.right = BTNode(7) 
    root.right.left.right = BTNode(8) 
    
    # node1 = root.left.right 
    # node2 = root.right.right  
    
    # print "Yes" if isCousin(root, node1, node2) == 1 else "No"

    a = levelTraversal(root, 0)
    print(a)