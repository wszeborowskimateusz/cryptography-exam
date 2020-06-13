def euclides(a, b):
    x, x_prim, y, y_prim = 1, 0, 0, 1
    while b != 0:
        q = a // b
        r = b
        b = a%b
        a = r
        t = x_prim
        x_prim = x - q*x_prim
        x = t
        t = y_prim
        y_prim = y - q*y_prim
        y = t
    return (a, x, y)

def solve_equation(a, b, n):
    d, y, z = euclides(a, n)
    if d == 1:
        x0 = (y * b) % n
        print(f"Solution: x = {x0} +- k*{n}")
        return x0
    if d > 1:
        if b % d != 0:
            print("There are no solutions")
            return None
        else:
            x0 = y * b // d
            print(f"Solution: x = {x0} +- k * {n//d}")
            return x0

# solve_equation(4238479232, 12, 745947598363612)
# solve_equation(868224, 1, 1064359)
