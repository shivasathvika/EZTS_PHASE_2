#binary tree traversal using recursive method
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def inorder(root):
    if root:
        #1st recur on lc
        inorder(root.left)
        #then prnt data of node
        print(root.val,end=" ")
        #now recur on rc
        inorder(root.right)
def postorder(root):
    if root:
        #1st recur on lc
        postorder(root.left)
        #now recur on rc
        postorder(root.right)
        #then prnt data of node
        print(root.val,end=" ")
def preorder(root):
    if root:
        #then prnt data of node
        print(root.val,end=" ")
        #1st recur on lc
        preorder(root.left)
        #now recur on rc
        preorder(root.right)
root=Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.left.right.left=Node(900)
root.right.left=Node(800)
root.right.right=Node(200)
root.right.right.left=Node(300)
print("Pre-order")
preorder(root)
print()
print("\nIn-order")
inorder(root)
print()
print("\nPost-order")
postorder(root)
print()
        
