import timeit

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def wrapper(func,*args,**kwargs):
    def wrapped():
        return func(*args,**kwargs)
    return wrapped


def binomial(n,k):
    if n==k or k==0:
        return 1
    return binomial(n-1,k)+binomial(n-1,k-1) #Bad recursion here, you don't store the previous data and compute the result repeatedly

binomial2=Memoize(binomial)

# def binomialDynamic(n,k):
#     bino=[[0 for x in range(n+1)] for x in range(k+1)]
#     for i in range(n+1):
#         for j in range(min(k,i)+1):
#             if j==i or j==0:
#                 bino[i][j]=1
#             else:
#                 bino[i][j]=bino[i-1][j-1]+bino[i-1][j]
#     return bino[n][k]

def binomialCoef(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]

    # Calculate value of Binomial Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1

            # Calculate value using previosly stored values
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]

    return C[n][k]

wrapped1=wrapper(binomial,100,15)
wrapped2=wrapper(binomial2,100,15)


# print("The time for normal recursion is {}".format(timeit.timeit(wrapped1,number=1000)))
# print("The time for memory recursion is {}".format(timeit.timeit(wrapped2,number=1000)))
print(binomial2(10,2))
print(binomialCoef(10,2))
#The time for normal recursion is 0.018936439002573024
# The time for memory recursion is 0.0013711799983866513

# The time for normal recursion is 20.27983268900425
# The time for memory recursion is 0.026218669998343103
