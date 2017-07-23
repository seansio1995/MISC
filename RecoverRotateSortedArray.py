class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def reverse(self,nums):
        if len(nums)==0:
            return nums
        start, end =0, len(nums)-1
        while start < end:
            tmp=nums[start]
            nums[start]=nums[end]
            nums[end]=tmp
            start+=1
            end-=1
        return nums
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                a=self.reverse(nums[0:i+1])
                b=self.reverse(nums[i+1:len(nums)])
                c=self.reverse((a+b))
        return c

    def recoverRotatedSortedArray2(self, nums):
        # write your code here
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         a=self.reverse(nums[0:i+1])
        #         b=self.reverse(nums[i+1:len(nums)])
        #         c=self.reverse((a+b))
        # return c
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                a=nums[0:i+1]
                b=nums[i+1:len(nums)]
        return (b+a)


if __name__=="__main__":
    s=Solution()
    nums=[4,5,1,2,3]
    rec=s.recoverRotatedSortedArray2(nums)
    print(rec)
