def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n


def testCase():
    assert factorial(5)==120
    assert factorial(1)==1
    assert factorial(0)==1
    assert factorial(3)==6


if __name__=="__main__":
    testCase()
