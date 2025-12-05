import numpy as np


def solve(data):
    return sum((np.cumsum([x for r in data.split() for x in [{'R': 1, 'L': -1}[r[0]]] * int(r[1:])]) + 50) % 100 == 0)


DATA0 = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

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
