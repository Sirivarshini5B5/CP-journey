class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class dll:
    def __init__(self):
        self.head=None
    def insertatbegining(self,newdata):
        if self.head is None:
            newnode=node(newdata)
            self.head=newnode
            newnode.left=None
            newnode.right=None
        else:
            newnode=node(newdata)
            newnode.left=None
            newnode.right=self.head
            self.head=newnode
    def insertatend(self,newdata):
        newnode=node(newdata)
        if self.head is None:
            self.head=newnode
            newnode.left=None
            newnode.right=None
        else:
            last=self.head
            while last.right is not None:
                last=last.right
            newnode.left=last
            last.right=newnode
            newnode.right=None
    def insertatposition(self,newdata,pos):
        newnode=node(newdata)
        i=1
        last=self.head
        fast=last.right
        flag=0
        while fast is not self.head:
            if i==pos:
                flag=1
                break
            fast=fast.right
            last=last.right
            i+=1
        if flag==1:
            newnode.left=last
            last.right=newnode
            last.right.right=fast
            fast.left=newnode
    def display(self):
        temp=self.head
        while(temp):
            print(str(temp.data)+" ",end="")
            temp=temp.right
    def deleteatbegining(self):
        if self.head is None:
            return
        else:
            self.head=self.head.right
            self.head.left=None
    def deleteatend(self):
        if self.head is None:
            return
        else:
            last=self.head
            while last.right.right is not None:
                last=last.right
            last.right=None
    def deleteatposition(self,pos):
        i=1
        last=self.head
        fast=self.head.right
        flag=0
        while fast.right is not self.head:
            if i==pos:
                flag=1
                break
            i+=1
            last=last.right
            fast=fast.right
        if flag==1:
            last.right=fast.right
            fast.left=last
        else:
            return "not found"
    def search(self,val):
        current=self.head
        while current is not None:
            if current.data == val:
                return True
            current=current.right
        return False
    
d=dll()
print("insertion at beginning:")
d.insertatbegining(3)
d.display()
print("\ninsertion at beginning:")
d.insertatbegining(2)
d.display()
print("\ninsertion at beginning:")
d.insertatbegining(1)
d.display()
print("\ninsertion at end:")
d.insertatend(4)
d.display()
print("\ninsertion at postion:")
d.insertatposition(5,2)
d.display()
print("\ndelete at beginning:")
d.deleteatbegining()
d.display()
print("\ndelete at end:")
d.deleteatend()
d.display()
print("\ndelete at postion:")
d.deleteatposition(1)
d.display()
print("\n element to be searched:")
d.search(3)
d.display()
