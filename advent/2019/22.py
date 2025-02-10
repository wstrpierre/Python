from functools import cache

N1, N2, R = 10007, 119315717514047, 101741582076661


def euclide(a, b):
    if a:
        q, r = divmod(b, a)
        x, y = euclide(r, a)
        return y - q * x, x
    else:
        return 0, 1


def get_coeffs(data, n):
    a, b = 1, 0
    for row in data.splitlines():
        if row.startswith('deal with increment'):
            k = int(row.split()[-1])
            a, b = a * k % n, b * k % n
        elif row.startswith('cut'):
            b = (b - int(row.split()[-1])) % n
        else:
            a, b = -a % n, (-b - 1) % n
    return a, b


@cache
def recurse_coeffs(a, b, n, r=R):
    if r:
        if r % 2:
            a0, b0 = recurse_coeffs(a, b, n, r - 1)
            return a * a0 % n, a * b0 + b % n
        else:
            a0, b0 = recurse_coeffs(a, b, n, r // 2)
            return a0 ** 2 % n, b0 * (1 + a0) % n
    else:
        return 1, 0


def solve(data):
    (a1, b1), (a2, b2) = get_coeffs(data, N1), recurse_coeffs(*get_coeffs(data, N2), N2)
    return (a1 * 2019 + b1) % N1, euclide(a2, N2)[0] * (2020 - b2) % N2


DATA1 = '''deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1'''

DATA2 = '''cut 6
deal with increment 7
deal into new stack'''

DATA3 = '''deal with increment 7
deal into new stack
deal into new stack'''

DATA4 = '''deal with increment 7
deal with increment 9
cut -2'''

DATA0 = DATA4
DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 64586600795606
