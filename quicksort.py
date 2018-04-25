def quicksort(nums):
      ##remind me of two pointers
      helper(nums,0,len(nums)-1)


def helper(nums,first,last):
    if first < last:
        splitpoint=partition(nums,first,last)
        helper(nums,first,splitpoint-1)
        helper(nums,splitpoint+1,last)


def partition(nums,first,last):
    pivot=nums[first]
    left=first+1
    right=last

    done=False
    while not done:
        while left<=right and nums[left] <= pivot:
            left+=1

        while left<=right and nums[right] >= pivot:
            right-=1

        if right < left:
            done=True
        else:
            tmp=nums[left]
            nums[left]=nums[right]
            nums[right]=tmp
    tmp=nums[first]
    nums[first]=nums[right]
    nums[right]=tmp

    return right


import random
nums=random.sample(range(100),12)
print(nums)
quicksort(nums)
print(nums)
