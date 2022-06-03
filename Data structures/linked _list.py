class node:
    def __init__(self,item):
        self.item=item
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
        
    def insertatbegining(self,new_item):
        new_node=node(new_item)
        new_node.next=self.head
        self.head=new_node
        
    def insertatend(self,new_item):
        new_node=node(new_item)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next is not None):
            last=last.next
        last.next=new_node
        
        
    def insertatposition(self,prev_node,new_item):
        if prev_node is None:
            print("the given previos node mustin linked list")
            return
        new_node=node(new_item)
        new_node.next=prev_node.next
        prev_node.next=new_node
        
        
    def deletenode(self,position):
        if self.head is None:
            return
        temp=self.head
        if position == 0:
            self.head=temp.next
            temp=None
            return
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
        
        
    def search(self,key):
        current=self.head
        while current is not None:
            if current.item==key:
                return True
            current=current.next
        return False
        
        
    def sortlinkedlist(self,head):
        current=head
        index=node(None)
        if head is None:
            return
        else:
            while current is not None:
                index=current.next
                while index is not None:
                    if current.item>index.item:
                        current.item,index.item=index.item,current.item
                    index=index.next
                current=current.next
                
                
    def printlist(self):
        temp=self.head
        while(temp):
            print(str(temp.item),end=" ")
            temp=temp.next
        
if __name__== '__main__':
    linked_list=linkedlist()
    linked_list.head=node(1)
    second=node(2)
    third=node(3)
    linked_list.head.next=second
    second.next=third
    linked_list.printlist()
    print()
    linked_list.insertatbegining(4)
    linked_list.printlist()
    print()
    linked_list.insertatend(5)
    linked_list.printlist()
    print()
    linked_list.insertatposition(linked_list.head.next,6)
    linked_list.printlist()
    print()
    linked_list.deletenode(3)
    linked_list.printlist()
    print()
    item_to_find=3
    if linked_list.search(item_to_find):
        print(str(item_to_find)+" is found")
    else:
        print(str(item_to_find)+" is not found")
    print()
    linked_list.sortlinkedlist(linked_list.head)
    print("sorted list:")
    linked_list.printlist()
