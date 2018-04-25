def insertionsort(nums):
    for i in range(1,len(nums)):
        current=nums[i]
        position=i
        while position >0 and nums[position-1] > current:
            nums[position]=nums[position-1]
            position-=1

        nums[position]=current

    return nums


import random
nums=random.sample(range(100),12)
print(nums)
print("Nums after sorting")
print(insertionsort(nums))
