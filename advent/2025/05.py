def solve(data):
    raw_rngs, raw_ids = data.split('\n\n')
    rngs = sorted(tuple(map(int, row.split('-'))) for row in raw_rngs.splitlines())
    ids = [*map(int, raw_ids.splitlines())]
    fresh_ids = set()
    for i in ids:
        for a, b in rngs:
            if a <= i <= b:
                fresh_ids.add(i)

    rngs = [[a, b + 1] for a, b in rngs]
    m = 0
    for rng in rngs:
        for i, x in enumerate(rng):
            m = max(m, x)
            rng[i] = m

    return sum(b - a for a, b in rngs)


DATA0 = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

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
