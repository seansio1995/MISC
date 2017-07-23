def selectionsort(nums):
    for pivot in range(len(nums)-1,0,-1):
        posMax=0
        for location in range(1,pivot+1):
            if nums[location] > nums[posMax]:
                posMax=location

        tmp=nums[pivot]
        nums[pivot]=nums[posMax]
        nums[posMax]=tmp



import random
nums=random.sample(range(100),12)
print(nums)
selectionsort(nums)
print(nums)
