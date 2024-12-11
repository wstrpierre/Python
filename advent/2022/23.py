def display(positions):
    i_min, i_max = int(min(pos.real for pos in positions)), int(max(pos.real for pos in positions))
    j_min, j_max = int(min(pos.imag for pos in positions)), int(max(pos.imag for pos in positions))
    for i in range(i_min - 1, i_max + 2):
        print('  '.join('.#'[complex(i, j) in positions] for j in range(j_min - 1, j_max + 2)))


N = 10000


def solve(data):
    orients = [-1, 1, -1j, 1j]
    positions = {complex(i, j) for i, row in enumerate(data.split()) for j, c in enumerate(row) if c == '#'}

    def get_target(pos):
        if {pos + z * o for z in (1, 1 + 1j) for o in orients} & positions:
            for o in orients:
                if not {pos + o * complex(1, i) for i in (-1, 0, 1)} & positions:
                    return pos + o
        return pos

    print(f'\n\nInitial State:')
    display(positions)

    for r in range(N):
        print(f'Round {r + 1}...')
        targets = {p: get_target(p) for p in positions}

        target_count = {}
        for target in targets.values():
            target_count[target] = target_count.get(target, 0) + 1

        dups = {target for target, count in target_count.items() if count > 1}
        targets = {pos: pos if tgt in dups else tgt for pos, tgt in targets.items()}

        if all(pos == tgt for pos, tgt in targets.items()):
            return r + 1

        positions = {*targets.values()}
        orients = [*orients[1:], orients[0]]

        # print(f'\n\nRound {r + 1}:')
        # display(positions)

    raise ValueError
    # i_min, i_max = min(pos.real for pos in positions), max(pos.real for pos in positions)
    # j_min, j_max = min(pos.imag for pos in positions), max(pos.imag for pos in positions)
    # return int((i_max - i_min + 1) * (j_max - j_min + 1) - len(positions))


DATA0 = '''..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............'''

DATA1 = '''.....
..##.
..#..
.....
..##.
.....'''

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
