def solve(data):
    n = 0
    for row in data.split('\n'):
        policy, pwd = row.split(': ')
        str_interval, c = policy.split()
        x0, x1 = map(int, str_interval.split('-'))
        # n += x0 <= pwd.count(c) <= x1
        n += (pwd[x0 - 1] == c) + (pwd[x1 - 1] == c) == 1
    return n


DATA0 = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''

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
