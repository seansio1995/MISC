def shellsort(nums):
    gapcount=len(nums)//2
    while gapcount >0:
        for start in range(gapcount):
            gap_insertion_sort(nums,start,gapcount)

        gapcount=gapcount//2



def gap_insertion_sort(nums,start,gapcount):
    for i in range(start+gapcount,len(nums),gapcount):
        current=nums[i]
        pos=i

        while pos >=gapcount and nums[pos-gapcount] > current:
            nums[pos]=nums[pos-gapcount]
            pos-=gapcount

        nums[pos]=current

arr = [45,67,23,45,21,24,7,2,6,4,90]
shellsort(arr)
print(arr)
