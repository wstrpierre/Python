M, S = 20201227, 7


def solve(data):
    (key0, key1), val, key = map(int, data.split()), 1, 1
    while val != key1:
        key, val = (key * key0) % M, (val * S) % M
    return key


DATA0 = '''5764801
17807724'''

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
