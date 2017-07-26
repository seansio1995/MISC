def index_prod(nums):
    output=[None]*len(nums)
    product=1
    i=0

    while i < len(nums):
        output[i]=product
        product*=nums[i]
        i+=1

    product=1
    i=len(nums)-1
    while i>=0:
        output[i]*=product
        product*=nums[i]
        i-=1
    return output



print(index_prod([1,2,3,4]))
print(index_prod([0,1,2,3,4]))
