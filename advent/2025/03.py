def max_joltage(bank, n=11):
    if n:
        x = max(bank[:-n])
        i = bank.index(x)
        return x * 10 ** n + max_joltage(bank[i + 1:], n - 1)
    else:
        return max(bank)


def solve(data):
    banks = [[*map(int, row)] for row in data.splitlines()]
    return sum(map(max_joltage, banks))


DATA0 = '''987654321111111
811111111111119
234234234234278
818181911112111'''

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
