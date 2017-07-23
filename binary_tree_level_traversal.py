class Solution:
    def levelOrder(self,root):
        self.results=[]
        if results is None:
            return self.results

        q=[root]

        while q:
            new_q=[]
            self.results.append([p.val for p in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)

                q=new_q

        return self.results
