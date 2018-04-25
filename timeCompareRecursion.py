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

def factorial(n):
    if n<2:
        return 1
    return factorial(n-1)*n

factorial2=Memoize(factorial)

wrapped=wrapper(factorial,100)
wrapped2=wrapper(factorial2,100)

print("The time for normal recursion is {}".format(timeit.timeit(wrapped,number=1000)))
print("The time for memory recursion is {}".format(timeit.timeit(wrapped2,number=1000)))

#The time for normal recursion 0.027422825922258198
# The time for memory recursion 0.0015980800380930305
