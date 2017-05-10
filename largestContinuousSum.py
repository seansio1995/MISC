def large_cont_sum(arr):
    if len(arr)==0:
        return 0
    maxsum=currentsum=arr[0]

    for num in arr[1:]:
        currentsum=max(currentsum+num,num)
        maxsum=max(maxsum,currentsum)
    return maxsum


def testCase():
    assert large_cont_sum([1,2,-1,3,4,-1])==9
    assert large_cont_sum([2,3,2,-1,-4,3,2])==7
    assert large_cont_sum([-1,1])==1


if __name__=="__main__":
    testCase()
