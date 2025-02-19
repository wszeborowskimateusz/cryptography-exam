import numpy as np
import math
from functools import reduce

def perm_pow(perm, pow):
    n = len(perm)
    if pow == 0:
        return list(range(1, n + 1))
    if pow < 0:
        pow = -1 * pow
        old_perm = perm.copy()
        for i in range(n):
            perm[i] = old_perm.index(i + 1) + 1

    new_perm = []
    for i in range(n):
        calculated_val = perm[i]
        for _ in range(pow - 1):
            calculated_val = perm[calculated_val - 1]
        new_perm.append(calculated_val)
    return new_perm
    

def mul(*perms):
    if len(perms) <= 0:
        return

    for i in range(len(perms[0])):
        calculated_val = perms[0][i] 
        for j in range(1, len(perms)):
            calculated_val = perms[j][calculated_val - 1]
        yield calculated_val

def get_cycles(pi):
    n = len(pi)
    k = 0
    cycles = []
    v = np.full(n, False)

    for i in range(n):
        if not v[i] and pi[i] != (i + 1):
            k, s = k + 1, i
            v[s] = True
            cycles.append([pi[s]])

            while not v[pi[s] - 1]:
                v[pi[s] - 1], s = True, pi[s] - 1
                cycles[-1].append(pi[s])
    return k, cycles

def lcm(*args):
    def __lcm(a, b):
        return abs(a*b) // math.gcd(a, b)
    return reduce(__lcm, args)

def find_k(perm):
    cycles = get_cycles(perm)
    cycle_lengths = [len(x) for x in cycles[1]]
    return lcm(*cycle_lengths)

def get_perm_from_cycles(n, *cycles):
    perms = [x + 1 for x in list(range(n))]
    shifteds = []
    for cycle in cycles:
        for index, elem in enumerate(cycle):
            perms[elem - 1] = cycle[(index + 1)% len(cycle)]
    return perms


# print(perm_pow([4, 2, 1, 3, 5], -2))

# print(list(mul([4, 2, 1, 3, 5], [3, 2, 1, 4, 5], [5, 4, 3, 2, 1])))

# print(find_k([5, 8, 10, 3, 1, 2, 9, 6, 4, 7]))

# print(perm_pow(get_perm_from_cycles(32, (1,29,21,4,8,13,28,22,14,19,3,16,11),(2,26,32,10,6,23,15,25),(5,31),(7,20,17,12,24,18,9,27)), 3))
# print(perm_pow(get_perm_from_cycles(32, (1,29,21,4,8,13,28,22,14,19,3,16,11),(2,26,32,10,6,23,15,25),(5,31),(7,20,17,12,24,18,9,27)), -1))
# print(get_perm_from_cycles(32, (1,29,21,4,8,13,28,22,14,19,3,16,11),(2,26,32,10,6,23,15,25),(5,31),(7,20,17,12,24,18,9,27))[19])
# print(find_k(get_perm_from_cycles(32, (1,29,21,4,8,13,28,22,14,19,3,16,11),(2,26,32,10,6,23,15,25),(5,31),(7,20,17,12,24,18,9,27))))

print(lcm(len((1,29,21,4,8,13,28,22,14,19,3,16,11)),len((2,26,32,10,6,23,15,25)),len((5,31)),len((7,20,17,12,24,18,9,27))))