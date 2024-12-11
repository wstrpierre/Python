def solve(data):
    mask, mem, shifts = [], {}, []
    for row in data.split('\n'):
        cmd, val = row.split(' = ')
        if cmd == 'mask':
            shifts, mask = [0], int(val.replace('X', '1'), 2)
            for i, c in enumerate(val[::-1]):
                if c == 'X':
                    shifts += [2 ** i + s for s in shifts]
        else:
            mem_id, x = int(cmd[4:-1]) | mask, int(val)
            for shift in shifts:
                mem[mem_id - shift] = x

    return sum(mem.values())


DATA0 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

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
