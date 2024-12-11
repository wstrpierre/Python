DIRS = {'E': 1, 'N': 1j, 'W': -1, 'S': -1j}
TURNS = {'L': 1, 'R': -1}


def solve(data):
    # pos, orient = 0j, 1 + 0j
    pos, orient = 0j, 10 + 1j
    for row in data.split():
        c, x = row[0], int(row[1:])
        if c == 'F':
            pos += x * orient
        elif c in 'LR':
            orient *= (TURNS[c] * 1j) ** (x // 90)
        else:
            # pos += x * DIRS[c]
            orient += x * DIRS[c]

    return abs(int(pos.imag)) + abs(int(pos.real))


DATA0 = '''F10
N3
F7
R90
F11'''

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
