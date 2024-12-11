import numpy as np
from scipy.ndimage import convolve


def solve(data):
    grid = np.array([['XMAS'.index(c) for c in row] for row in data.split()])
    w = 10 ** np.array([[1, 0, 2], [0, 3, 0], [4, 0, 5]]) // 10
    return sum((convolve(grid, w, mode='constant', cval=0) == x).sum() for x in (11233, 13213, 31231, 33211))


DATA0 = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

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
