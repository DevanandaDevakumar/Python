# no unwanted memory wastage
# ll has data and reference of next object
# link created in compile time
# eg: undo redo button
# singly linked list, doubly ll,circular ll
# application of ll,trees and graphs?

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=Node(40)
# head.next.next.next.next=Node(50)

#Instead

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
        

l1=LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.display()

# Traversal

#temp=head

# while temp.next!=None:
#     print(temp.data,"->",end=" ")
#     temp=temp.next
# print(temp.data)

# while temp.next:
#     print(temp.data,"->",end=" ")
#     temp=temp.next
# print(temp.data)

# while temp:
#     print(temp.data,end=" ")
#     temp=temp.next

# while temp:
#     print(temp.data,end="->")
#     temp=temp.next
# print(None)