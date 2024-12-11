import numpy as np


def add(p0, p1):
    return p0[0] + p1[0], p0[1] + p1[1]


MOVES = (-1, 0), (1, 0), (0, -1), (0, 1)


def solve(data):
    state = [[*map('.^v<>'.index, row[1:-1])] for row in data.split()[1:-1]]
    l, w = len(state), len(state[0])

    def run(start=(0, 0), target=(l - 1, w - 1), shift=0):
        positions = set()
        for n in range(shift, 1000):
            def is_valid(p):
                i, j = p
                if not (0 <= i < l and 0 <= j < w):
                    return False
                elif state[(i + n) % l][j] == 1:
                    return False
                elif state[(i - n) % l][j] == 2:
                    return False
                elif state[i][(j + n) % w] == 3:
                    return False
                elif state[i][(j - n) % w] == 4:
                    return False
                else:
                    return True

            positions = {*filter(is_valid, positions | {start, *(add(p, m) for m in MOVES for p in positions)})}

            if target in positions:
                return n + 1

    n0 = run()
    n1 = run((l - 1, w - 1), (0, 0), n0)
    return run(shift=n1)


DATA0 = '''#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''

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
