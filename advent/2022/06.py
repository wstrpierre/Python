N = 14


def solve(data):
    return next(i for i, x in enumerate(zip(*(data[i:] for i in range(N)))) if len({*x}) == N) + N


DATA0 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

DATA = open(__file__.removesuffix('.py') + '.txt').readlines()[0]


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6

    print(f'Solution ====> {solution} | Calc time = {calc_time} ms.')


if __name__ == '__main__':
    main(False)
