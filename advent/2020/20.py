import numpy as np
from math import prod
from scipy.ndimage import convolve

MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


def get_edge_ids(t):
    return [min(sum(x * 2 ** i for i, x in enumerate(s)) for s in (side, reversed(side)))
            for side in (t[0], t[:, -1], t[-1], t[:, 0])]


def solve(data):
    tiles = {int(part[0].split()[1][:-1]): np.array([[*map('#'.__eq__, row)] for row in part[1:]], int)
             for part in (part.split('\n') for part in data.split('\n\n'))}
    edges, links = {k: get_edge_ids(tile) for k, tile in tiles.items()}, {}
    for k, edge_ids in edges.items():
        for e in edge_ids:
            links.setdefault(e, []).append(k)
    links = {e: v for e, v in links.items() if len(v) == 2}
    corners = [k for k, edge_ids in edges.items() if len({*edge_ids} & {*links}) == 2]
    n = int(len(tiles) ** .5)
    for i in range(n):
        if i:
            t0 = tile_map[i - 1, 0]
            e0 = edges[t0][2]
            t1 = next(filter(t0.__ne__, links[e0]))
            r = (- edges[t1].index(e0)) % 4
            tiles[t1], edges[t1] = np.rot90(tiles[t1], -r), [*np.roll(edges[t1], r)]
            while any(tiles[t0][-1] != tiles[t1][0]):
                tiles[t1] = tiles[t1][:, ::-1]
                edges[t1][1], edges[t1][3] = edges[t1][3], edges[t1][1]
            tile_map[i, 0] = t0 = t1
        else:
            t0 = next(k for k, edge_ids in edges.items() if len({*edge_ids} & {*links}) == 2)
            r = next(i for i in range(4) if all(map(links.get, np.roll(edges[t0], i)[1:3])))
            tiles[t0], edges[t0] = np.rot90(tiles[t0], -r), [*np.roll(edges[t0], r)]
            tile_map = np.zeros((n, n), int)
            tile_map[0, 0] = t0

        for j in range(1, n):
            e0 = edges[t0][1]
            t1 = next(filter(t0.__ne__, links[e0]))
            r = 3 - edges[t1].index(e0)
            tiles[t1], edges[t1] = np.rot90(tiles[t1], -r), [*np.roll(edges[t1], r)]
            while any(tiles[t0][:, -1] != tiles[t1][:, 0]):
                tiles[t1] = tiles[t1][::-1]
                edges[t1][0], edges[t1][2] = edges[t1][2], edges[t1][0]
            tile_map[i, j] = t0 = t1

    # for k in range(n):
    #     np.pad()
    #     tiles[tile_map[k, 0]] = tiles[tile_map[k, 0]]
    #     tiles[tile_map[k, -1]] = tiles[tile_map[k, -1]][:, :-1]
    #     tiles[tile_map[0, k]] = tiles[tile_map[0, k]][1:]
    #     tiles[tile_map[-1, k]] = tiles[tile_map[-1, k]][:-1]
    # for i in range(1, n - 1):
    #     for j in range(1, n - 1):
    #         tiles[tile_map[i, j]] = tiles[tile_map[i, j]][1:-1, 1:-1]
    # for t, tile in tiles.items():
    #     tile[t] = tile[1:-1, 1:-1]
    grid = np.concatenate([np.concatenate([tiles[t][1:-1, 1:-1] for t in row], axis=1) for row in tile_map])
    # m = len(grid) // n
    # for d in (0, 1):
    #     grid = np.delete(grid, [i * m - k for i in range(1, n) for k in (0, 1)], d)

    pattern = np.array([[*map('#'.__eq__, row)] for row in MONSTER.split('\n')], int)

    x0 = np.zeros((5, 5), int)
    x0[1:4, 1:4] = 1
    w0 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], int)
    x1 = convolve(x0, w0) == w0.sum()
    x2 = convolve(x1, w0) * 1

    patterns = [np.rot90(p, i) for i in range(4) for p in (pattern, pattern.T)]

    x = np.zeros(grid.shape, bool)
    for p in patterns:
        x |= convolve(grid, p, int, 'constant', 0) == p.sum()


    # return prod(corners)
    return grid.sum() - x.sum() * pattern.sum()


DATA0 = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''

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
