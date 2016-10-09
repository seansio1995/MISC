#find the sum of all left leaves in a given binary Tree

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        sum=self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        if root.left!=None and root.left.left==None and root.left.right==None:
            sum+=root.left.val
        return sum
