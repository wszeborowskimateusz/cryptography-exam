import math
from functools import reduce

def count_divisors(a):
    result = 0
    for b in range(1, a + 1):
        result += math.floor(a // b) - math.floor((a - 1) // b)
    return result

def fast_pow(a, b):
    c = 1
    while b > 0:
        if b % 2  != 0:
            c *= a
        a = a ** 2
        b = b // 2
    return c

def amount_of_bits(a):
    if a == 0: return 1
    return math.log(math.sqrt(a)) + 1

def sqrt(a, b):
    if a == 1 or b == 1: return a
    if b > amount_of_bits(a): return 1
    l, p = 1, a
    while l <= p -2:
        s = math.floor((l + p) // 2)
        if math.pow(s, b) <= a:
            l = s
        else:
            p = s
    return l


def nww(*args):
    return reduce(lambda a, b: a * b // math.gcd(a, b), args)

def nwd(*args):
    return reduce(lambda a, b: math.gcd(a, b), args)

# |ab| = nwd(a, b) * nww(a, b).

# ϕ(p^n) = p^n − p^(n−1)
# Jeśli liczby naturalne a, b są względnie pierwsze, to
# ϕ(ab) = ϕ(a)ϕ(b).

def euler(a):
    result = 0
    print(f"Calculating Euler function for {a}")
    for i in range(2, a):
        print(f"Trying {i}")
        if nwd(i, a) == 1:
            result += 1
    return result
# https://www.alpertron.com.ar/ECM.HTM
def euler2(n):
    print(f"Trying to calculate euler for {n}")
    # Initialize result as n 
    result = n;  
  
    # Consider all prime factors 
    # of n and subtract their 
    # multiples from result 
    p = 2;  
    while(p * p <= n): 
        print(f"Checking some shity n = {n} and p = {p} and p^2 = {p*p}")
        # Check if p is a  
        # prime factor. 
        if (n % p == 0):  
              
            # If yes, then  
            # update n and result 
            while (n % p == 0): 
                n = int(n / p); 
            result -= int(result / p); 
        p += 1; 
  
    # If n has a prime factor 
    # greater than sqrt(n) 
    # (There can be at-most  
    # one such prime factor) 
    if (n > 1): 
        result -= int(result / n); 
    return result;  
