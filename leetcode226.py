#Invert Binary Tree
#invert all the left nodes of tree to be right nodes
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
            return root
