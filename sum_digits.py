def sum_digits(n):
    if len(str(n))==1:
        return n
    return n%10+sum_digits(n//10)



def testCase():
    assert sum_digits(10)==1
    assert sum_digits(132)==6
    assert sum_digits(1995)==24

if __name__=="__main__":
    testCase()
