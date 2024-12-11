def solve(data):
    seq = [*map(int, data), 0]
    disk = []
    files = []
    spaces = []
    c = 0
    for i, (x0, x1) in enumerate(zip(seq[::2], seq[1::2]), 1):
        if x0:
            files.append([x0, c])
            c += x0
        if x1:
            if x0:
                spaces.append([x1, c])
            else:
                spaces[-1] += x1
            c += x1

    for f in files[::-1]:
        for s in spaces:
            if s[1] > f[1]:
                break
            if s[0] >= f[0]:
                spaces.append([*f])
                f[1] = s[1]
                s[1] += f[0]
                s[0] -= f[0]
                break

    return sum(i * (f[1] + j) for i, f in enumerate(files) for j in range(f[0]))


DATA0 = '''2333133121414131402'''

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
