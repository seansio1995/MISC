class Solution:
    def dailyTemperatures(self, nums):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res=list()
        for i in range(len(nums)):
            cnt=0
            flag=False
            for j in range(i+1,len(nums)):
                if nums[j]<=nums[i]:
                    cnt+=1
                else:
                    cnt+=1
                    flag=True
                    break
            if flag:
                res.append(cnt)
            else:
                res.append(0)
        return res


"""
Time Limit Exceed
"""
