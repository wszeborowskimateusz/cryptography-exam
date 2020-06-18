from extended_euclides import solve_equation

def zlicz_punkty(a, b,c, n):
    def zliczYY(n):
        kw={}
        for i in range(n):
            ii = pow(i, 2, n)
            kw[ii] = kw.setdefault(ii, 0) + 1
        return kw
    
    kw = zliczYY(n)
    result = 1
    for i in range(n):
        w = (i**3 + a*(i**2) + b*i + c) %n
        if w in kw: result += kw[w]

    return result

class ECPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"ECPoint({self.x}, {self.y})"

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def add_non_zero_points(a, b, n, p1, p2):
    if p1.x == p2.x and (p1.y + p2.y) % n == 0:
        print("Punkt 0")
        return None
    if p1.x == p2.x and (p1.y + p2.y) % n != 0:
        lambda_ = ((3*(p1.x ** 2) + a) * pow(2 * p1.y,-1, n)) % n
    else:
        lambda_ = (((p2.y - p1.y) % n) * pow(p2.x - p1.x,-1, n)) % n
    print(f"Lambda: {lambda_}")
    x3 = ((lambda_ ** 2) - p1.x - p2.x) % n
    y3 = ((p1.x - x3) * lambda_ - p1.y) % n
    return ECPoint(x3, y3)

# print(zlicz_punkty(672570, 2441148, 5584262, 10583389))
print(add_non_zero_points(6647178, 2012643, 10339163, ECPoint(9994180, 2062779), ECPoint(4648046, 2832530)))
print(add_non_zero_points(6647178, 2012643, 10339163, ECPoint(9994180, 2062779), ECPoint(9994180, 2062779)))
# print(add_non_zero_points(2, 5, 2051417, ECPoint(855702, 794259), ECPoint(1872044, 1219646)))
# print(add_non_zero_points(2, 5, 2051417, ECPoint(7840, 878140), ECPoint(1872044, 1219646)))