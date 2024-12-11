import re
from math import prod

PATTERN = re.compile('mul\(\d{1,3},\d{1,3}\)')


def solve(data):
    parts = [part.split('don\'t')[0] for part in data.split('do()')]
    return sum(prod(map(int, op[4:-1].split(','))) for part in parts for op in PATTERN.findall(part))


DATA0 = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

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
