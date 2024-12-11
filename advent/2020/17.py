import numpy as np
from scipy.ndimage import convolve

N = 6


def solve(data):
    cube = np.array([[[[*map('#'.__eq__, row)] for row in data.split()]]], int)
    w = np.ones((3, 3, 3, 3), int)
    w[1, 1, 1, 1] = 0
    for _ in range(N):
        cube = np.pad(cube, 1)
        neighbors = convolve(cube, w, int, 'constant')
        cube = cube & (neighbors == 2) | (neighbors == 3)
    return cube.sum()


DATA0 = '''.#.
..#
###'''

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
