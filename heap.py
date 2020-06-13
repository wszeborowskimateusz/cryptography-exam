import numpy as np

def heap(n):
    counter = 0
    i = 0
    c = np.zeros(n, dtype=int)
    pi = list(range(1, n+ 1))
    yield pi
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                pi[c[i]], pi[i] = pi[i], pi[c[i]]
            else:
                pi[0], pi[i] = pi[i], pi[0]
            yield pi
            counter+=1
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    print(f"Number of permutations: {counter + 1}")

print(list(heap(4)))