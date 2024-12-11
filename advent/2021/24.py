OP_FNS = {'add': 'add', 'mul': 'mul', 'div': 'floordiv', 'eql': 'eq', 'mod': 'mod'}
OPS = {op: getattr(int, f'__{fn}__') for op, fn in OP_FNS.items()}
VARS = 'xyz'


def parse(data):
    data_parts = [part.split('\n') for part in f'\n{data}'.split('\ninp w\n')[1:]]
    param_ids = [i for i, rows in enumerate(zip(*data_parts)) if len({*rows}) > 1]
    pattern = [[op, var, x if x.isalpha() else int(x)] for op, var, x in map(str.split, data_parts[0])]
    for i, pid in enumerate(param_ids):
        pattern[pid][-1] = f'#{i}'
    return pattern, [[int(part[i].split()[-1]) for i in param_ids] for part in data_parts]


def solve(data):
    pattern, params = parse(data)

    def alu(w, p, z=0):
        v = dict(zip(VARS, (0, 0, z)))
        for op, var, x in pattern:
            x = x if isinstance(x, int) else p[int(x[1])] if x[0] == '#' else w if x == 'w' else v[x]
            v[var] = int(OPS[op](v[var], x))
        return v['z']

    res = {0}
    for p0 in params:
        res = {alu(w0, p0, z0) for w0 in range(1, 10) for z0 in res}
        print(sorted(res))

    return len(res)


DATA0 = ''''''

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
