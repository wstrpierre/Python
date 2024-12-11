import numpy as np


def to_decimal(binary):
    return sum(x * 2 ** i for i, x in enumerate(binary[::-1]))


def solve(data):
    report = np.array([[*map(int, row)] for row in data.split()], int)
    oxy, co2 = report, report
    for i in range(oxy.shape[1]):
        oxy = oxy[oxy[:, i] == (oxy.mean(axis=0) >= .5)[i]]

    for i in range(co2.shape[1]):
        _co2 = co2[co2[:, i] == (co2.mean(axis=0) < .5)[i]]
        if len(_co2):
            co2 = _co2

    return to_decimal(oxy[0]) * to_decimal(co2[0])


DATA0 = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

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
