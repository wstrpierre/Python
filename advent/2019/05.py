I = 5


def solve(data):
    mem, p = [*map(int, data.split(','))], 0
    out = 0
    p = 0
    while mem[p] != 99:
        mcode, op = divmod(mem[p], 100)
        if op in (1,2,5,6,7,8):
            a, b, dest, p = mem[p + 1], mem[p + 2], mem[p + 3], p + 4
            mb, ma = divmod(mcode, 10)
            va, vb = a if ma else mem[a], b if mb else mem[b]
            if op==1:
                mem[dest]=va+vb
            elif op==2:
                mem
            mem[dest] = (int.__add__, int.__mul__)[op - 1](va, vb)
        elif op == 3:
            mem[mem[p + 1]], p = I, p + 2
        elif op in (4,5,6):
            mx = mcode % 10
            x, p = mem[p + 1], p + 2
            vx = x if mx else mem[x]
            print(f'Output = {vx}')
            out = vx
        else:
            raise ValueError
    return out


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
