from array import array

import numpy as np
from numpy.ma.core import argmax

N = 2000


def evolve(x):
    x ^= x << 6
    x &= (1 << 24) - 1
    x ^= x >> 5
    x &= (1 << 24) - 1
    x ^= x << 11
    return x & (1 << 24) - 1


def solve(data):
    a = np.array([*map(int, data.split())])
    r = np.zeros((N + 1, len(a)), np.int32)
    for i in range(N):
        r[i] = a % 10
        a = evolve(a)
    r[N] = a % 10
    d = r[1:] - r[:-1] + 9
    p = sum(d[k:N - 3 + k] * 32 ** k for k in range(4))
    c = np.zeros(32 ** 4, int)
    for r0, p0 in zip(r[4:].T, p.T):
        s = set()
        for r1, p1 in zip(r0, p0):
            if p1 not in s:
                c[p1] += r1
                s.add(p1)
    m = argmax(c)
    z = tuple((m>>(5*i))%32-9 for i in range(4))
    q = sum((x+9)*32**k for k,x in enumerate((-2,1,-1,3)))
    return c.max()


DATA0 = '''1
2
3
2024'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)
