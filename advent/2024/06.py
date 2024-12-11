import numpy as np


def solve(data):
    raw = np.array([[*row] for row in data.split()])
    obstructions, start = {complex(i, j) for i, j in np.argwhere(raw == '#')}, complex(*np.argwhere(raw == '^')[0])

    def run(obs):
        pos, orient, visited = start, -1, set()
        while 0 <= int(pos.real) < len(raw) and 0 <= int(pos.imag) < len(raw[0]) and (pos, orient) not in visited:
            visited.add((pos, orient))
            while pos + orient in obs:
                orient *= -1j
            pos += orient
        return {p[0] for p in visited} - {start}, (pos, orient) in visited

    return sum([run(obstructions | {z})[1] for z in run(obstructions)[0]])


DATA0 = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 1795 incorrect
