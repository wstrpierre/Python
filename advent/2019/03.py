import numpy as np


def solve(data):
    all_moves = [[1j ** 'RULD'.index(part[0]) for part in row.split(',') for _ in range(int(part[1:]))]
                 for row in data.split()]
    all_points = [*map(list, map(np.cumsum, all_moves))]
    inter = set.intersection(*map(set, all_points))
    return min(sum(points.index(x) for points in all_points) for x in inter) + 2


DATA0 = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83'''

DATA1 = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''

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
