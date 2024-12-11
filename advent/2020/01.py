X = 2020


def solve(data):
    d = [*map(int, data.split())]

    m = [(x, y, z)
         for i, x in enumerate(d[:-2])
         for j, y in enumerate(d[i + 1:-1], i + 1)
         for z in d[j + 1:]
         if x + y + z == X]
    return sum(x * y * z for x, y, z in m)


DATA0 = '''1721
979
366
299
675
1456'''

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
