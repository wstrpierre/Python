N = 10000000
S = 1000000


# N = 100
# S = 9


def solve(data):
    init = [*(int(c) - 1 for c in data), *range(len(data), S)]
    circle, cur, t, targets = [0] * S, init[0], init[0], [0] * 3
    for i, x in enumerate(init):
        circle[x] = init[(i + 1) % S]
    for i in range(N):
        if not i % 1000:
            print(i)
        for j in range(3):
            targets[j] = t = circle[t]
        dest = (cur - 1) % S
        while dest in targets:
            dest = (dest - 1) % S

        circle[cur], circle[t], circle[dest] = circle[t], circle[dest], targets[0]
        cur = t = circle[cur]

    return (circle[0] + 1) * (circle[circle[0]] + 1)
    # res, cur = 0, circle[0]
    # while cur:
    #     res, cur = res * 10 + cur + 1, circle[cur]
    # return res


DATA0 = '389125467'

DATA = '247819356'


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)
