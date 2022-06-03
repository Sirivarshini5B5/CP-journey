class node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val)+"->",end="")
        inorder(root.right)
def preorder(root):
    if root:
        print(str(root.val)+"->",end="")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+"->",end="")

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
print("inorder traversal:")
inorder(root)
print("\npreorder traversal:")
preorder(root)
print("\npostorder traversal:")
postorder(root)
