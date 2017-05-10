def add(a,b):
    return a+b

def testCase():
    assert add(1,2)==3
    assert add(2,3)==5
    assert add(3,4)==7
    assert add(3,3)==6

if __name__=="__main__":
    testCase()
