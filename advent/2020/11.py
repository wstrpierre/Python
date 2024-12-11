import numpy as np
from scipy.ndimage import convolve

N=5
def solve(data):
    seats = np.array([[*map('L'.__eq__, row)] for row in data.split()], bool)
    w, (used, adj) = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], int), (np.zeros(seats.shape, bool) for _ in range(2))
    dirs = np.array([[i, j] for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j])
    while (seats & (adj == 0) & ~used).any() or (used & (adj >=N )).any():
        used = used & (adj < N) | (adj == 0) & seats
        adjs = np.zeros((*seats.shape, len(dirs)), int)

        def fill(i, j, k):
            if 0 <= i < seats.shape[0] and 0 <= j < seats.shape[1]:
                if not adjs[i, j, k]:
                    i0, j0 = dirs[k] + (i, j)
                    if 0 <= i0 < seats.shape[0] and 0 <= j0 < seats.shape[1]:
                        adjs[i, j, k] = int(used[i0, j0]) + int(seats[i0, j0])
                    if not adjs[i, j, k]:
                        adjs[i, j, k] = fill(i0, j0, k)

                return adjs[i, j, k]
            else:
                return 1

        for i, j in zip(*np.where(seats)):
            for k in range(len(dirs)):
                fill(i, j, k)

        adj = (adjs//2).sum(axis=-1)
        # adj = convolve(used, w, int, 'constant') * seats + (1 - seats) * 9
    return used.sum()


DATA0 = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

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
