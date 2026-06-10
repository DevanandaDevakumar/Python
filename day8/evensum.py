class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
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
    def esum(self): # su of even numbers
        temp=self.head
        sum=0
        while temp:
            if temp.data%2==0:
                sum=sum+temp.data
            temp=temp.next
        print(sum)
    def cnt(self): #count of even no
        temp=self.head
        sum=0
        while temp:
            if temp.data%2==0:
                sum=sum+1
            temp=temp.next
        print(sum)
    def prime(self):
        temp = self.head
        while temp:
            f = 1
            if temp.data <= 1:
                print(temp.data, "is not prime no")
                temp = temp.next
                continue
            for i in range(2, int(temp.data**0.5) + 1):
                if temp.data % i == 0:
                    print(temp.data, "is not prime no")
                    f = 0
                    break
            if f:
                print(temp.data, "is prime no")
            temp = temp.next        

l1=LinkedList()
n=int(input("no of elements:"))
for i in range(n):
    l1.append(int(input()))
l1.display()
l1.esum()
l1.cnt()
l1.prime()