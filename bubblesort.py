def bubblesort(nums):
    n=len(nums)
    for i in range(n-1,0,-1):
        for k in range(i):
            if nums[k] > nums[k+1]:
                tmp=nums[k]
                nums[k]=nums[k+1]
                nums[k+1]=tmp
    return nums



#nums=[3,2,13,4,6,5,7,8,1,20]
import random
nums=random.sample(range(100),10)
print(nums)
print("After sorting")
print(bubblesort(nums))
