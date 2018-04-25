from math import sqrt,ceil

def get_primes(n):
    prime_list=[]
    for candidate in range(2,n+1):
        is_prime=True
        root=int(ceil(sqrt(candidate)))
        for prime in prime_list:
            if prime > root:
                break
            if candidate%prime == 0:
                is_prime=False
                break
        if is_prime:
            prime_list.append(candidate)
    return prime_list


print(get_primes(200))
