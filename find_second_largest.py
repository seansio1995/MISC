
class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# def find_largest(root):
#     if root is None:
#         raise Exception("Tree must have at least 1 node")
#     if root.right:
#         return find_largest(root.right)
#     return root.value
#
#
# def find_second_largest(root):
#     if root is None or (root.right is None and root.left is None):
#         raise Exception("Tree must have at least 2 nodes")
#
#     if root.left and not root.right:
#         return find_largest(root.left)
#
#     if root.right and not root.right.left and not root.right.right:
#         return root.value
#
#
#
#     return find_second_largest(root.right)



def find_largest(root):
    current=root
    while current:
        if not current.right:
            return current.value
        current=current.right



def find_second_largest(root):
    if root is None or (root.right is None and root.left is None):
        raise Exception("The tree must have at least 2 nodes")
    current=root

    while current:

        if current.left and not current.right:
            return find_largest(current.left)

        if current.right and not current.right.left and not current.right.right:
            return current.value
        current=current.right
