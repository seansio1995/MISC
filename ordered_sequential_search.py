def sequential_search(nums,target):
    pos=0
    found=False
    stopped=False

    while pos < len(nums) and not found and not stopped:
        if nums[pos]==target:
            found=True
        else:
            if nums[pos] > target:
                stopped=True
            else:
                pos+=1
    return found


import random
nums=random.sample(range(100),12)
nums.sort()

print(sequential_search(nums,nums[7]))
