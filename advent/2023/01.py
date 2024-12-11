def solve(data):
    for i, d in enumerate(('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'), 1):
        data = data.replace(d, f'{d}{i}{d}')
    return sum(int(f'{x[0]}{x[-1]}') for x in ([c for c in row if c.isnumeric()] for row in data.split()))


DATA0 = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

DATA1 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA1 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)
