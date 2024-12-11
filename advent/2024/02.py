import numpy as np


def solve(data: str):
    # d = [*map(int, data.splitlines())]
    d = [np.array([int(part) for part in row.split()]) for row in data.splitlines()]

    def _is_safe(r):
        x = r[1:] - r[:-1]
        return ((x > 0) & (x <= 3)).all() or ((x < 0) & (x >= -3)).all()

    def is_safe(r):
        if _is_safe(r):
            return True
        else:
            for i in range(len(r)):
                if _is_safe(np.array([*r[:i], *r[i + 1:]])):
                    return True
            return False


    return sum(map(is_safe, d))


DATA0 = ''''''

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
