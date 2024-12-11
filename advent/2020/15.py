N = 2020
N = 30_000_000


def solve(data):
    init = [*map(int, data.split(','))]
    state, head = {x: i for i, x in enumerate(init[:-1])}, init[-1]
    for i in range(len(state), N - 1):
        state[head], head = i, i - state.get(head, i)
    return head


DATA0 = '''0,3,6'''

DATA = '''19,0,5,1,10,13'''


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)
