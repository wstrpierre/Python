import numpy as np


def solve(data):
    signals = np.array([1, *(x for cmd in data for x in ([0] if cmd == 'noop' else [0, int(cmd.split()[1])]))]).cumsum()
    return '\n'.join(''.join(' ' if abs(j - x) > 1 else '#' for j, x in enumerate(signals[i * 40:(i + 1) * 40]))
                     for i in range(6))


DATA0 = ['addx 15', 'addx -11', 'addx 6', 'addx -3', 'addx 5', 'addx -1', 'addx -8', 'addx 13', 'addx 4', 'noop',
         'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx -35',
         'addx 1', 'addx 23.txt', 'addx -19', 'addx 1', 'addx 16.txt', 'addx -11', 'noop', 'noop', 'addx 21', 'addx -15',
         'noop', 'noop', 'addx -3', 'addx 9', 'addx 1', 'addx -3', 'addx 8', 'addx 1', 'addx 5', 'noop', 'noop', 'noop',
         'noop', 'noop', 'addx -36', 'noop', 'addx 1', 'addx 7', 'noop', 'noop', 'noop', 'addx 2', 'addx 6', 'noop',
         'noop', 'noop', 'noop', 'noop', 'addx 1', 'noop', 'noop', 'addx 7', 'addx 1', 'noop', 'addx -13', 'addx 13',
         'addx 7', 'noop', 'addx 1', 'addx -33', 'noop', 'noop', 'noop', 'addx 2', 'noop', 'noop', 'noop', 'addx 8',
         'noop', 'addx -1', 'addx 2', 'addx 1', 'noop', 'addx 17', 'addx -9', 'addx 1', 'addx 1', 'addx -3', 'addx 11',
         'noop', 'noop', 'addx 1', 'noop', 'addx 1', 'noop', 'noop', 'addx -13', 'addx -19', 'addx 1', 'addx 3',
         'addx 26', 'addx -30', 'addx 12', 'addx -1', 'addx 3', 'addx 1', 'noop', 'noop', 'noop', 'addx -9', 'addx 18',
         'addx 1', 'addx 2', 'noop', 'noop', 'addx 9', 'noop', 'noop', 'noop', 'addx -1', 'addx 2', 'addx -37',
         'addx 1', 'addx 3', 'noop', 'addx 15', 'addx -21', 'addx 22', 'addx -6', 'addx 1', 'noop', 'addx 2', 'addx 1',
         'noop', 'addx -10', 'noop', 'noop', 'addx 20', 'addx 1', 'addx 2', 'addx 2', 'addx -6', 'addx -11', 'noop',
         'noop', 'noop']

DATA = [x.replace('\n', '') for x in open(__file__.removesuffix('.py') + '.txt').readlines()]


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution:\n\n{solution}\n\nCalc time = {calc_time} ms.')


if __name__ == '__main__':
    # main()
    main(False)
