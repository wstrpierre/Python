import numpy as np


def solve0(data):
    z = sum({'f': 1j, 'u': -1, 'd': 1}[row[0]] * int(row.split()[-1]) for row in data.split('\n'))
    return int(z.real * z.imag)

def solve(data):
    d = np.array([{'f': 1j, 'u': -1, 'd': 1}[row[0]] * int(row.split()[-1]) for row in data.split('\n')], complex)
    return int((d.real.cumsum() * d.imag).sum() * d.imag.sum())

DATA0 = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''

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
