import time

def sumOfN(n):
    start=time.time()

    sum=0

    for i in range(1,n+1):
        sum=sum+i
    end=time.time()
    return sum,end-start

def sumOfN3(n):
    start=time.time()
    sum=n*(n+1)/2
    end=time.time()
    return sum,end-start

if __name__=="__main__":
    for i in range(5):
        print("Sum is %d required %10.7f seconds"%sumOfN(10000))
    print("Sum is %d required %10.7f seconds"%sumOfN3(10000))
