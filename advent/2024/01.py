def solve(data):
    x, y = {}, {}
    for i, j in [map(int, row.split()) for row in data.splitlines()]:
        x[i], y[j] = x.get(i, 0) + 1, y.get(j, 0) + 1
    return sum(i * k * y.get(i, 0) for i, k in x.items())


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
