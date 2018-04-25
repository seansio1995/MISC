memory={}

def factorial(n):
    if n<2:
        return 1
    if not n in memory:
        memory[n]=factorial(n-1)*n
    return memory[n]

print(factorial(4))
