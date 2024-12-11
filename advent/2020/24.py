ORIENTS = 2, 1 + 1j, -1 + 1j, -2, -1 - 1j, 1 - 1j
N = 100


def solve(data):
    data = data.replace('ne', '1').replace('nw', '2').replace('se', '5').replace('sw', '4')
    data = data.replace('e', '0').replace('w', '3')
    tiles = set()
    for row in data.split():
        t = sum(ORIENTS[int(c)] for c in row)
        if t in tiles:
            tiles.remove(t)
        else:
            tiles.add(t)

    for _ in range(N):
        tiles_off, nb_count = set(), {}
        for t in tiles:
            neighbors = {t + o for o in ORIENTS}
            if len(neighbors & tiles) not in (1, 2):
                tiles_off.add(t)
            for nb in neighbors:
                nb_count[nb] = nb_count.get(nb, 0) + 1
        tiles |= {nb for nb, x in nb_count.items() if x == 2}
        tiles -= tiles_off

    return len(tiles)


DATA0 = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main() # 10 | 2208
    main(False)  # 322
