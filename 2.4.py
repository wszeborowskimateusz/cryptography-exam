from math import gcd
from functools import lru_cache, reduce


def lcm(*args):
    return reduce(lambda a, b: a * b // gcd(a, b), args)


@lru_cache(maxsize=None)
def divisions(n):
    def generator():
        if n < 2:
            return

        yield (n,)

        for i in range(1, n):
            left = divisions(i)
            right = divisions(n - i)

            for l in left:
                for r in right:
                    yield l + r

    return set(generator())

def cycles(c):
    i = 1
    for cycle in c:
        yield f"({' '.join(map(str, range(i, i + cycle)))})"
        i += cycle

n = 10
pairs = set()
numbers = dict()

if __name__ == "__main__":
    for l in range(0, 11):
        for d in divisions(n - l):
            pair = (lcm(*d), l)
            pairs.add(pair)
            numbers[pair] = d

for p in pairs:
    print(p, ": ", " ".join(cycles(numbers[p])))