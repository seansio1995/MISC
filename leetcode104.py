#104. Maximum Depth of Binary Tree
#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node

class Solution(object):
    def maxDepth(self,root):
            return 0 if root==None else  max(self.maxDepth(root.left),self.maxDepth(root.right))+1
#if root has no node at all return 0
#else root has at least 1 depth and we keep traversing through left node and right node
