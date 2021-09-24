# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# An XOR linked list is a more memory efficient doubly linked list. 
# Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
# Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), 
# you can assume you have access to get_pointer and dereference_pointer 
# functions that converts between nodes and memory addresses.

# so implement a D-L-L with XOR `both` instead of next
# two classes for Node and DLL (so the LL data structure can process the XOR op)
# add(elem) -> adds to right end
# get(index) -> returns node

import ctypes

class Node:
    "A node to hold data in a DLL"

    def __init__(self, data):
        self.data = data
        self.npx = 0 # XOR of prev and next nodes

class XorLinkedList:
    "A Doubly Linked List of Nodes"

    def __init__(self):
        self.head = None
        self.nodes = []

    def XOR(self, a, b):
        "Returns XORed value of the node addresses"

        return(a ^ b)

    def insert(self, data):
        "Insert a new node in the head of the XLL"

        node = Node(data)
        node.npx = id(self.head) # XOR of head and 0
        if self.head is not None:
            self.head.npx = self.XOR(id(node),self.head.npx)
            self.nodes.append(node)
        self.head = node 

    def printList(self):
        "Prints the XLL self in Forward (L->R) order"

        if self.head != None:
            prev_id = 0
            curr = self.head
            next_id = 1

            while curr is not None:
                print(curr.data, end = ' ')
                next_id = self.XOR(prev_id, curr.npx)
                prev_id = id(curr)
                curr = self.__type_cast(next_id)

    def __type_cast(self, id):
        "Return new instance of type of data"

        return ctypes.cast(id, ctypes.py_object).value

if __name__ == "__main__":

    # head <-> 1<-> 2 <-> 3 <-> 4 <-> 5
    xor = XorLinkedList()
    xor.insert(1)
    xor.insert(2)
    xor.insert(3)
    xor.insert(4)
    xor.insert(5)
