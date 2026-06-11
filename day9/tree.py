# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def inorder(self,t):
#         if(t):
#             t.inorder(t.left)
#             print(t.data,end=" ")
#             t.inorder(t.right)
#         return 
#     def preorder(self,t):
#         if(t):
#             print(t.data,end=" ")
#             t.inorder(t.left)
#             t.inorder(t.right)
#         return 
#     def postorder(self,t):
#         if(t):
#             t.inorder(t.left)
#             t.inorder(t.right)
#             print(t.data,end=" ")
#         return 
# t=Node(10)
# t.left=Node(20)
# t.right=Node(30)
# t.left.left=Node(40)
# t.left.right=Node(50)
# t.right.left=Node(60)
# t.right.right=Node(70)
# t.inorder(t)
# t.preorder(t)
# t.postorder(t)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self, t):
        if not t:
            return []
        return self.inorder(t.left) + [t.data] + self.inorder(t.right)

    def preorder(self, t):
        if not t:
            return []
        return [t.data] + self.preorder(t.left) + self.preorder(t.right)

    def postorder(self, t):
        if not t:
            return []
        return self.postorder(t.left) + self.postorder(t.right) + [t.data]

t = Node(10)
t.left = Node(20)
t.right = Node(30)
t.left.left = Node(40)
t.left.right = Node(50)
t.right.left = Node(60)
t.right.right = Node(70)

print("Inorder:", *t.inorder(t))
print("Preorder:", *t.preorder(t))
print("Postorder:", *t.postorder(t))