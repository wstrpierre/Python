TARGET = 19690720
# TARGET = 4930687


def solve(data):
    prog = [*map(int, data.split(','))]

    def run(x):
        mem = [*prog]
        mem[1:3] = x // 100, x % 100
        for i in range(0, len(mem), 4):
            op, a, b, dest = mem[i:i + 4]
            if op == 99:
                return mem[0]
            elif op in (1, 2):
                mem[dest] = (int.__add__, int.__mul__)[op - 1](mem[a], mem[b])
            else:
                return 0

    return next(x for x in range(10000) if run(x)==TARGET)
    # return run(1202)


DATA0 = '1,9,10,3,2,3,11,0,99,30,40,50'

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 4930687
