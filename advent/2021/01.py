N = 3

def solve(data):
    numbers = [*map(int, data.split())]
    numbers = [*map(sum, zip(*(numbers[i:] for i in range(N))))]
    return sum(x0 < x1 for x0, x1 in zip(numbers, numbers[1:]))


DATA0 = '''199
200
208
210
200
207
240
269
260
263'''

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
