import numpy as np


def solve(data):
    grid = np.array([[*row] for row in data.split()])
    nodes, n = [[*map(complex, *np.argwhere(grid == a).T)] for a in {*grid[grid != '.']}], len(grid)
    anti = {z0 + k * (z1 - z0) for grp in nodes for z0 in grp for z1 in grp for k in range(n)}
    return sum(0 <= z.real < n and 0 <= z.imag < n for z in anti)


DATA0 = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

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
