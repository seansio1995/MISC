class Solution:
    def invertTree(self,root):
        if root is None:
            return None
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root
