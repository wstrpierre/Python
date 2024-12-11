from functools import cache

N = 75


@cache
def count(x, depth=N):
    if depth:
        if x == 0:
            return count(1, depth - 1)
        elif not len(str(x)) % 2:
            return count(int(str(x)[:len(str(x)) // 2]), depth - 1) + count(int(str(x)[len(str(x)) // 2:]), depth - 1)
        else:
            return count(x * 2024, depth - 1)
    else:
        return 1


def solve(data):
    return sum(map(count, map(int, data.split())))


DATA0 = '125 17'

DATA = '0 37551 469 63 1 791606 2065 9983586'


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 36345101551476 False
