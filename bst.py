class BSTNode:

  def __init__(self, key):
    self.val = key
    self.left = None
    self.right = None


def insert(root, key):
  if root is None:
    return BSTNode(key)
  if key < root.val:
    root.left = insert(root.left, key)
  else:
    root.right = insert(root.right, key)
  return root


def inorder(root):
  if root:
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


# Driver Code
root = None
keys = [50, 30, 70, 20, 40, 60, 80]
for k in keys:
  root = insert(root, k)

print("Inorder Traversal (Sorted BST):", end=" ")
inorder(root)
print()