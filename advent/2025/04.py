import numpy as np
from scipy.ndimage import convolve


def solve1(data):
    grid = np.array([[*map('@'.__eq__, row)] for row in data.split()], int)
    return ((convolve(grid, np.ones((3, 3)), mode='constant') < 5) & grid).sum()


def solve2(data):
    grid, res, n_removed = np.array([[*map('@'.__eq__, row)] for row in data.split()], bool), 0, 1
    while n_removed:
        removed = (convolve(grid * 1, np.ones((3, 3)), mode='constant') < 5) & grid
        grid ^= removed
        n_removed = removed.sum()
        res += n_removed
    return res


solve = solve2

DATA0 = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

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
