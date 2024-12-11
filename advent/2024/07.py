def solve(data):
    equations = [(int(row.split(': ')[0]), [*map(int, row.split(': ')[1].split())]) for row in data.splitlines()]

    def match(tgt, vals):
        if len(vals) == 1:
            return vals[0] == tgt
        else:
            return max(
                match(tgt, [vals[0] + vals[1], *vals[2:]]),
                match(tgt, [vals[0] * vals[1], *vals[2:]]),
                match(tgt, [int(f'{vals[0]}{vals[1]}'), *vals[2:]])
            )

    return sum(match(tgt, vals) * tgt for tgt, vals in equations)


DATA0 = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

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
