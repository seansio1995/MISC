def twoSum7(nums, target):
        # write your code here
        nums=[(num,i) for i,num in enumerate(nums)]
        target=abs(target)
        n, index=len(nums),[]

        nums=sorted(nums, key=lambda x:x[0])

        # i=0
        # j=1
        # while i<n and j<n:
        #     if nums[j][0]-nums[i][0]==target:
        #         index=[nums[j][1]+1,nums[i][1]+1]
        #     elif nums[j][0]-nums[i][0] < target:
        #         j+=1
        #     else:
        #         i+=1
        #
        # if index[0] > index[1]:
        #     index[0],index[1]=index[1],index[0]
        # return index
        return nums

print(twoSum7([2,7,15,24],5))
