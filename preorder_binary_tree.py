class Solution:


    def preorderTraversal(self,root):
        if root is None:
            return []
        preorder=[]
        stack=[root]

        while stack:
            node=stack.pop()
            preorder.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)  ##be careful, left has to be pop out first, so it has to be append later than right
        return preorder
