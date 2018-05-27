class Solution(object):
    def pascal(self,num):
        res=[[1]]
        for i in range(1,num):
            res.append(list(map(lambda x,y:x+y,[0]+res[-1],res[-1]+[0])))
        return res



if __name__=="__main__":
    a=Solution()
    print(a.pascal(8))
