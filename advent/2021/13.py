import numpy as np
from numpy.ma.core import shape


def solve(data):
    str_points, str_fold = data.replace('fold along ', '').replace('=', '').split('\n\n')
    points = [tuple(map(int, row.split(','))) for row in str_points.split()]
    paper = np.zeros([*map((1).__add__, map(max, zip(*points)))], bool)
    for p in points:
        paper[p] = True

    for orient, x in ((row[0] == 'y', int(row[1:])) for row in str_fold.split()):
        n = paper.shape[orient]
        if orient:
            paper[:, 2 * x - n + 1:x] |= paper[:, n:x:-1]
            paper = paper[:, :x]
        else:
            paper[2 * x - n + 1:x] |= paper[n:x:-1]
            paper = paper[:x]

    print('\n'.join('  '.join(('  ', '##')[c] for c in row) for row in paper.T))
    return 0


DATA0 = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''

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
