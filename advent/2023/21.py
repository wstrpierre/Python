# from functools import cache
from time import time_ns

STEPS = 26501365


def solve(data):
    size = len(data)
    if not size % 2:
        raise ValueError('Even size')
    rocks = {(i, j) for i, line in enumerate(data) for j, c in enumerate(line) if c == '#'}
    start = next((i, j) for i, line in enumerate(data) for j, c in enumerate(line) if c == 'S')

    s = start[0]
    corners = (0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)

    # if {*range(1, size - 1)} - {i for i, j in rocks} or {*range(1, size - 1)} - {j for i, j in rocks}:
    #     raise ValueError('No rock on every rows or columns')

    def is_valid(p):
        # return (p[0] % max_i, p[1] % max_j) not in rocks
        if 0 <= p[0] < size and 0 <= p[1] < size:
            return p not in rocks
        else:
            return False

    def get_neighbours(p):
        return {*filter(is_valid, ((p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)))}

    def get_distances(s):
        distances, n_steps, pending = {}, 0, {s}
        while pending:
            distances |= {p: n_steps for p in pending}
            pending = {p0 for p in pending for p0 in get_neighbours(p) if p0 not in distances}
            n_steps += 1
        return distances

    start_dists = get_distances(start)
    corners_dists = {p: get_distances(p) for p in corners}

    max_corners_dists = max(dist for dists in corners_dists.values() for dist in dists.values())
    if max_corners_dists > (size - 1) * 2:
        raise ValueError(max_corners_dists)

    is_odd = s % 2
    n_even = sum(dist % 2 == is_odd for dist in start_dists.values())
    n_odd = len(start_dists) - n_even

    mid_dists = {p: get_distances(p) for p in [(0, s), (size, s), (s, 0), (s, size)]}

    if (STEPS - s) % size:
        raise ValueError('Invalid Step Count')

    q = (STEPS - s) // size

    corner_steps = size - s - 2
    n_corners = sum(dist % 2 == corner_steps % 2 and dist <= corner_steps
                    for dists in corners_dists.values() for dist in dists.values())

    res = n_even * (q - q % 2 + 1) ** 2 + n_odd * (q + q % 2) ** 2
    n_excl = sum(dist % 2 == is_odd and dist > s for dist in start_dists.values())
    res -= (q + 1) * n_excl
    res += q * n_corners
    print('Done.')

    return res


DATA0 = ['...........',
         '.....###.#.',
         '.###.##..#.',
         '..#.#...#..',
         '....#.#....',
         '.##..S####.',
         '.##..#...#.',
         '.......##..',
         '.##.#.####.',
         '.##..##.##.',
         '...........']
DATA = open(__file__.removesuffix('.py') + '.txt').readlines()

t0 = time_ns()
solution = solve(DATA)
calc_time = (time_ns() - t0) / 1e6

bounds = 610158174216258, 610158935066598
print(f'Solution ====> {solution:.0f} | Calc time = {calc_time} ms.')

if not bounds[0] < solution < bounds[1]:
    print('/!\\ Incorrect Solution (not within bounds).')

# 610,158,174,216,258 too low
# 610,158,935,066,598 too high
# 610,163,442,512,898 too high
