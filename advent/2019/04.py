A, B = 347312, 805915


def is_valid(x):
    has_same = False
    x0 = x
    (x, d0), r = divmod(x, 10), 0
    while x:
        x, d = divmod(x, 10)
        if d > d0:
            return False
        if d == d0:
            r += 1
        else:
            has_same |= r == 1
            r = 0
        d0 = d
    return has_same | (r == 1)


def solve():
    return sum(map(is_valid, range(A, B)))


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve()
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    main()
    # main(False) 196 too low
