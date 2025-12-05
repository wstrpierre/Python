def is_invalid(x):
    y = str(x)
    n = len(y)
    for q in range(2, n + 1):
        if not n % q:
            d = n // q
            s0 = y[:d]
            if all(s0 == y[d * i:d * (i + 1)] for i in range(1, q)):
                return True
    return y[:len(y) // 2] == y[len(y) // 2:]


def solve(data):
    ranges = [tuple(map(int, rng.split('-'))) for rng in data.split(',')]
    return sum(is_invalid(x) * x for a, b in ranges for x in range(a, b + 1))


DATA0 = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

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
