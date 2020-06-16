from sympy import Symbol
from sympy import div, add

x = Symbol('x')

def pol_div(p1,p2, mod):
    q,r = div(p1,p2,x)
    return q.as_poly(x,domain=f'GF({mod})'), r.as_poly(x,domain=f'GF({mod})')

def pol_add(p1,p2,mod):
    return add(p1,p2,x).as_poly(x,domain=f'GF({mod})')

