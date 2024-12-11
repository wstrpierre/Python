import numpy as np


def solve(data):
    (x0, x1), (y0, y1) = tuple(tuple(map(int, part[2:].split('..'))) for part in data[13:].split(', '))
    min_x = int(round(((1 + 4 * 2 * x0) ** .5) / 2))

    x_speed_0 = np.array(range(min_x, x1 + 1), int)
    y_speed_0 = np.array(range(y0, 1 - y0), int)
    x_speed = x_speed_0.copy()
    y_speed = y_speed_0.copy()
    x_pos = np.zeros(x_speed.shape, int)
    y_pos = np.zeros(y_speed.shape, int)

    shots = set()
    while len(y_speed):
        x_pos += x_speed
        y_pos += y_speed
        x_speed -= x_speed > 0
        y_speed -= 1
        x_valid = x_pos <= x1
        y_valid = y_pos >= y0
        x_pos = x_pos[x_valid]
        y_pos = y_pos[y_valid]
        x_speed = x_speed[x_valid]
        y_speed = y_speed[y_valid]
        x_speed_0 = x_speed_0[x_valid]
        y_speed_0 = y_speed_0[y_valid]
        shots |= {(x, y) for x in x_speed_0[x_pos >= x0] for y in y_speed_0[y_pos <= y1]}

    return len(shots)


DATA0 = '''target area: x=20..30, y=-10..-5'''

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
