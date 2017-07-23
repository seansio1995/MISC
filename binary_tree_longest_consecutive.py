class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive(self, root):
        # Write your code here
        return self.helper(root,None,0)

    def helper(self,root,parent,length):
        if root is None:
            return 0

        if parent is not None and parent.val+1==root.val:
            length+=1
        else:
            length=1      ###      Be Careful!! must set length back to 1 if it fails to be consecutive; for
            ###Example, it stays to be 2 and maybe updated to 3

        left=self.helper(root.left,root,length)
        right=self.helper(root.right,root,length)

        return max(length,max(left,right))
