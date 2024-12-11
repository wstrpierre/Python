def get_fuel(x):
    fuel = max(x // 3 - 2, 0)
    return fuel + (get_fuel(fuel) if fuel else 0)


def solve(data):
    return sum(map(get_fuel, map(int, data.split())))


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)
