import re
from math import gcd

ORIENT = U, R, D, L = (-1, 0), (0, 1), (1, 0), (0, -1)


def add(p0, p1):
    return p0[0] + p1[0], p0[1] + p1[1]


def parse(data):
    m, p = data.split('\n\n')
    path = [*zip(map({'R': 1, 'L': -1}.get, re.split(r'\d+', f'R{p}')[:-1]), map(int, re.split('[LR]', p)))]
    walk_map = m.split('\n')
    max_j = max(map(len, walk_map))
    return [row.ljust(max_j) for row in walk_map], path


def _connect(face_map, face_id, orient, side):
    face = face_map[face_id]
    if face[orient] >= 0:
        return True
    pivot_id = face[(orient + side) % 4]
    if pivot_id < 0:
        return False
    pivot = face_map[pivot_id]
    target_id = pivot[(pivot.index(face_id) + side) % 4]
    if target_id < 0:
        return False
    target = face_map[target_id]
    target[(target.index(pivot_id) + side) % 4] = face_id
    face[orient] = target_id


def connect(face_map, face_id, orient):
    for side in (-1, 1):
        if _connect(face_map, face_id, orient, side):
            return True
    return False


def fold(face_map):
    done = True
    for face_id in range(6):
        for orient in range(4):
            done &= connect(face_map, face_id, orient)
    if not done:
        fold(face_map)


def get_pattern(walk_map):
    l, w = len(walk_map), max(map(len, walk_map))
    n = gcd(l, w)
    face_ids = [(i, j) for i in range(l // n) for j in range(w // n) if walk_map[i * n][j * n] != ' ']
    id_map = {p: i for i, p in enumerate(face_ids)}
    pattern = [[id_map.get(add(p, o), -1) for o in ORIENT] for p in face_ids]
    fold(pattern)
    faces = [[[*map('.'.__eq__, row[j * n: (j + 1) * n])] for row in walk_map[i * n: (i + 1) * n]] for i, j in face_ids]
    print('\n'.join(''.join(map(str, row)) for row in pattern).replace('-1', '#'))
    return pattern, faces


def solve(data):
    walk_map, path = parse(data)
    pattern, faces = get_pattern(walk_map)
    n = max(map(len, faces))
    face_id, pos, orient = 0, (0, 0), 0

    for turn, dist in path:
        orient = (orient + turn) % 4
        for _ in range(dist):
            i, j = add(pos, ORIENT[orient])

            if 0 <= i < n and 0 <= j < n:
                f = face_id
            else:
                i %= n
                j %= n
                f = pattern[face_id][orient]
                o = (pattern[f].index(face_id) + 2) % 4

            if faces[face_id][i][j]:
                pos = i, j


DATA0 = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''

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
