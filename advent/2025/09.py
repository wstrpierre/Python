from bisect import bisect_left


def solve1(data):
    raw = [tuple(map(int, row.split(','))) for row in data.splitlines()]
    return max((abs(x1 - x0) + 1) * (abs(y1 - y0) + 1) for x0, y0 in raw for x1, y1 in raw)


def sort_segments(segments):
    segs_x, segs_y = [], []
    for (x0, y0), (x1, y1) in segments:
        if x0 == x1:
            segs_x.append((x0, (min(y0, y1), max(y0, y1))))
        else:
            segs_y.append((y0, (min(x0, x1), max(x0, x1))))
    return sorted(segs_x), sorted(segs_y)


def solve2(data):
    raw = [tuple(map(int, row.split(','))) for row in data.splitlines()]
    segs_x, segs_y = sort_segments([*zip(raw, (*raw[1:], raw[0]))])
    areas = [((abs(x1 - x0) + 1) * (abs(y1 - y0) + 1), ((x0, x1), (y0, y1)))
             for i, (x0, y0) in enumerate(raw[:-1]) for x1, y1 in raw[i + 1:]]

    def is_valid(rect):
        (x0, x1), (y0, y1) = map(sorted, rect)
        i_min, i_max = (bisect_left(segs_x, (x, (0, 0))) for x in (x0 + 1, x1))
        for x, (y_min, y_max) in segs_x[i_min: i_max]:
            if y_min <= y0 < y_max:
                return False
            if y_min < y1 <= y_max:
                return False

        j_min, j_max = (bisect_left(segs_y, (y, (0, 0))) for y in (y0 + 1, y1))
        for y, (x_min, x_max) in segs_y[j_min: j_max]:
            if x_min <= x0 < x_max:
                return False
            if x_min < x1 <= x_max:
                return False

        return True

    return next(area for area, rect in sorted(areas, reverse=True) if is_valid(rect))


solve = solve2

DATA0 = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

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
