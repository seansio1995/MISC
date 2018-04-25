def fib_rec(n):
    if n==0 or n==1:
        return 1
    return fib_rec(n-1)+fib_rec(n-2)


def fib_iter(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a

def testCase():
    assert fib_iter(1)==1
    assert fib_iter(10)==55
    assert fib_iter(23)==28657


if __name__=="__main__":
    testCase()
