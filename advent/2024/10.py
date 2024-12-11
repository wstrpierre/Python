import numpy as np
from networkx import neighbors
from scipy.ndimage import convolve


def solve(data):
    grid = np.array([[*map(int, row)] for row in data.split()])
    links = convolve(grid, [[0, 8000, 0], [400, -8421, 20], [0, 1, 0]], mode='constant')
    nbs = sum((links % 20 ** (k + 1) // 20 ** k == 1) * k ** 2 for k in range(4))
    network = {i for i in range(n) for j in range(n) for k in range(4) if links[i, j]}
    x = {}
    n = len(grid)
    print(grid)
    zeros = np.argwhere(grid == 0)

    def neighbors(i, j):
        nbs = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
        return [(_i, _j) for _i, _j in nbs if 0 <= _i < n and 0 <= _j < n and grid[_i, _j] - grid[i, j] == 1]

    def tails(i, j):
        if grid[i, j] == 9:
            return [(i, j)]
        else:
            return [p for _i, _j in neighbors(i, j) for p in tails(_i, _j)]

    return sum(len(tails(*p)) for p in zeros)


DATA0 = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    main()
    # main(False)
