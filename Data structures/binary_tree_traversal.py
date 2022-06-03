class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    def traversepreorder(self):
        print(self.val,end="->")
        if self.left:
            self.left.traversepreorder()
        if self.right:
            self.right.traversepreorder()
    def traverseinorder(self):
        if self.left:
            self.left.traverseinorder()
        print(self.val,end="->")
        if self .right:
            self.right.traverseinorder()
    def traversepostorder(self):
        if self.left:
            self.left.traversepostorder()
        if self.right:
            self.right.traversepostorder()
        print(self.val,end="->")

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
print("inorder traversal:")
root.traverseinorder()
print("\npreorder traversal:")
root.traversepreorder()
print("\npostorder traversal:")
root.traversepostorder()
