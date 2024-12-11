import numpy as np
from scipy.sparse.csgraph import dijkstra


def to_xy(z):
    return int(z.real), int(z.imag)


def solve(data):
    raw = np.array([[*map(ord, row)] for row in data.split()], int)
    grid = raw != ord('#')
    map_keys = (raw - ord('a') + 1) * ((raw >= ord('a')) & (raw <= ord('z')))
    map_doors = (raw - ord('A') + 1) * ((raw >= ord('A')) & (raw <= ord('Z')))

    start = complex(*np.argwhere(raw == ord('@'))[0])
    key_ids = {complex(x, y): map_keys[x, y] - 1 for x, y in np.argwhere(map_keys)}
    door_ids = {complex(x, y): map_doors[x, y] - 1 for x, y in np.argwhere(map_doors)}

    points = {*key_ids, *door_ids}
    dists = np.ones((len(points), len(points))) * np.inf

    def get_dists(p0):
        frontier, visited, dist, res = {p0}, set(), 0, {p0: 0}

        while frontier:
            visited |= frontier
            frontier = {p + 1j ** k for p in frontier for k in range(4) if grid[to_xy(p + 1j ** k)]} - visited
            dist += 1
            res |= {p: dist for p in frontier & points}
            frontier -= points

        return res

    start_dists = get_dists(start)
    n = len(key_ids)
    for _p0 in points:
        k0 = key_ids.get(_p0, door_ids.get(_p0, 0) + n)
        for _p1, _dist in get_dists(_p0).items():
            dists[k0, key_ids.get(_p1, door_ids.get(_p1, 0) + n)] = _dist

    d0 = dists * np.inf
    d0[:n, :n] = dists[:n, :n]

    def optimize(k, d):
        d = d.copy()
        tgts = np.argwhere((d[k] > 0) & (d[k] != np.inf))
        return 0

    return min(x0 + optimize(k) for k, x0 in start_dists.items())


DATA0 = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    main()
    # main(False)
