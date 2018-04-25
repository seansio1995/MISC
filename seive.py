def primes(x):
    prime=[]
    not_prime=[]
    for i in range(2,x+1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i*i,x+1,i):
                not_prime.append(j)
    return prime

#print(primes(30))
