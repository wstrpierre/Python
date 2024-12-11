def compute(expr):
    val = 0
    for c in expr:
        if c == ')':
            return val
        elif c == '*':
            return val * compute(expr)
        elif c == '(':
            val += compute(expr)
        else:
            val += int(c)
    return val


def solve(data):
    return sum(compute(iter(row)) for row in data.replace(' ', '').replace('+', '').split('\n'))


DATA0 = '''1 + 2 * 3 + 4 * 5 + 6'''

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
