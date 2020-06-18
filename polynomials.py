from sympy import Symbol
from sympy import div, add, ZZ
from sympy.polys.galoistools import gf_gcdex, gf_strip

x = Symbol('x')

def pol_div(p1,p2, mod):
    q,r = div(p1,p2,x, domain=f'GF({mod})')
    return q.as_poly(x,domain=f'GF({mod})'), r.as_poly(x,domain=f'GF({mod})')

def pol_add(p1,p2,mod):
    return add(p1,p2,x).as_poly(x,domain=f'GF({mod})')

# p1 - poli in <>
# p2 - poli ot inverse
# keep in mind to reverse p1 and p2 - Pan podaje odwrotnie
def gf_inv(p1,p2,m):
    res = gf_gcdex(gf_strip(p2), p1, m, ZZ)
    if res[2] != [1]:
        print("Nie ma odwrotnego")
    return res[0]

print(gf_inv([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], [1,0,0,1,1], 2))


