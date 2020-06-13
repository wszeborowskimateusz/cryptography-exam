def miller_rabin(p, a):
    n = p - 1
    cnt = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1
    
    x = pow(a, n, p)

    if x == 1 or x == p - 1:
        return True
    
    while cnt > 1:
        x = pow(x, 2, p)
        cnt -= 1
        if x == p - 1:
            return True
        if x == 1:
            return False
    return False

print(miller_rabin(117987841, 2))