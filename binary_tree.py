"""
This code creates a simple binary tree in python with an implementation of 
in-order, pre-order and post-order traversal algorithms.

written by: Arjang Fahim
Last update: 2/7/2021

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BTree:

    def __init__(self, data):
        self.root = Node(data)
        self.root.left = None
        self.root.right = None

    def add_node(self, root,  data):

        if root == None:
            return Node(data)

        if data > root.data:
            root.right = self.add_node( root.right ,data)
        else:
            root.left = self.add_node( root.left ,data)    

        return root

        
    def add_data(self, data):
        self.add_node(self.root, data)


    def preorder_utils(self, node):

        if node:
            print(node.data, end=" ")
            self.preorder_utils(node.left)
            self.preorder_utils(node.right)
        
    def preorder(self):
        self.preorder_utils(self.root)


    def inorder_utils(self, node):

        if node:
            self.inorder_utils(node.left)
            print(node.data, end = " ")
            self.inorder_utils(node.right)


    def inorder(self):
        self.inorder_utils(self.root)


    def postorder_utils(self, node):
        if node:
            self.postorder_utils(node.left)
            self.postorder_utils(node.right)
            print(node.data, end = " ")

    def postorder(self):
        self.postorder_utils(self.root)
    
    
             
btree = BTree(50)
btree.add_data(30)
btree.add_data(20)
btree.add_data(40)
btree.add_data(70)
btree.add_data(60)
btree.add_data(80)

btree.preorder()
print("\n")
btree.inorder()
print("\n")
btree.postorder()
