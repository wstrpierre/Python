def solve1(data):
    state, *diagram = [{i for i, c in enumerate(row) if c != '.'} for row in data.splitlines()[::2]]
    res = 0
    for splitters in diagram:
        res += len(state & splitters)
        state = {k for i in splitters & state for k in (i - 1, i + 1)} | (state - splitters)
    return res


def solve2(data):
    init, *diagram = [{i for i, c in enumerate(row) if c != '.'} for row in data.splitlines()[::2]]
    state = [int(i in init) for i in range(max(diagram[-1]) + 2)]
    for splitters in diagram:
        for i in splitters:
            state[i + 1] += state[i]
            state[i - 1] += state[i]
            state[i] = 0
    return sum(state)


solve = solve2

DATA0 = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

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
