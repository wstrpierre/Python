from functools import cache

TARGET = 21


@cache
def get_dice_map(n=3, depth=2):
    if depth:
        dice_map = {}
        for i, x in get_dice_map(n, depth - 1).items():
            for j, y in get_dice_map(n, 0).items():
                dice_map[i + j] = dice_map.get(i + j, 0) + x * y
        return dice_map
    else:
        return {i + 1: 1 for i in range(n)}


DICE_MAP = get_dice_map()


@cache
def win_counts(scores, pos, k):
    for i, score in scores:
        if score >= TARGET:
            return 1 - i, i

    counts = [0, 0]
    for i,x in DICE_MAP.items():
        pos = tuple(p + k0 for k0, p in enumerate(pos))
    res = [win_counts() for i in range(3)]


def solve(data):
    n, i, scores, pos = 0, 1, [0, 0], [*data]
    while scores[i] < TARGET:
        i = 1 - i
        for _ in range(3):
            pos[i] = (pos[i] + n % 100 + 1) % 10
            n += 1
        scores[i] += pos[i] + 1
    return scores[1 - i] * n


DATA0 = 3, 7
DATA = 0, 9


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)
