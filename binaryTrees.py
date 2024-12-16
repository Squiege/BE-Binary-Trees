class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Ordering the nodes
def in_order_traversal(node):
    if node is None:
        return 

    in_order_traversal(node.left)
    print(node.value, end=" ")
    in_order_traversal(node.right)

def pre_order_traversal(node):
    if node is None:
        return
    
    print(node.value, end=" ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

def post_order_traversal(node):
    if node is None:
        return

    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.value, end=" ")

# Nodes
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(40)
root.left.right = Node(20)
root.right.left = Node(60)
root.right.right = Node(80)

# Printing Traversals

# Post order Traversal
print("Post order Traversal of the tree:")
post_order_traversal(root)
print("")

# In order Traversal
print("In order Traversal of the tree:")
in_order_traversal(root)
print("")

# Pre order Traversal
print("Pre order Traversal of the tree:")
pre_order_traversal(root)