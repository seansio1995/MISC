def recur_Sum(n):
    if n==0:
        return 0
    return recur_Sum(n-1)+n


def testCase():
    assert recur_Sum(5)==15
    assert recur_Sum(10)==55
    assert recur_Sum(9)==45



if __name__=="__main__":
    testCase()
