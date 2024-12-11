def solve(data):
    schedule, a, n = [*map(int, data.split()[1].replace('x', '1').split(','))], -1, 1
    for b in schedule:
        a, n = next((a + i * n + 1, n * b) for i in range(b) if not (a + i * n + 1) % b)
    return a + 1 - len(schedule)


DATA0 = '''939
7,13,x,x,59,x,31,19'''

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
