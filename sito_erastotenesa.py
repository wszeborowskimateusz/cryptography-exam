import math

def erasto(n):
    A = (n - 2) * [True]
    for i in range(2, math.ceil(math.sqrt(n))):
        if A[i - 2] == True:
            for j in range(i * i, n - 2, i):
                print(f"Crossing {j - 2}")
                A[j - 2] = False
    return [i + 2 for i, v in enumerate(A) if v == True]

print(erasto(120))