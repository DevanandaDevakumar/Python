class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,node,data):
        if node is None:
            return Node(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        elif data>node.data:
            node.right=self.insert(node.right,data)
        return node
    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        print(root.data,end=" ") 
        self.inorder(root.right)

tree=BST()
tree.root=tree.insert(tree.root,5)
tree.root=tree.insert(tree.root,3)
tree.root=tree.insert(tree.root,1)
tree.root=tree.insert(tree.root,2)
tree.inorder(tree.root)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert(self.root, data)

#     def _insert(self, root, data):
#         if data < root.data:
#             if root.left is None:
#                 root.left = Node(data)
#             else:
#                 self._insert(root.left, data)
#         elif data > root.data:
#             if root.right is None:
#                 root.right = Node(data)
#             else:
#                 self._insert(root.right, data)

#     def inorder(self, root):
#         if root is None:
#             return
#         self.inorder(root.left)
#         print(root.data, end=" ")
#         self.inorder(root.right)

# tree = BST()
# tree.insert(5)
# tree.insert(3)
# tree.insert(1)
# tree.insert(2)

# tree.inorder(tree.root)