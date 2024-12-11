def solve(data):
    base_seq = [*map(int, data)]
    seq = [*base_seq]
    n = len(base_seq)
    index = {x: i for i, x in enumerate(base_seq)}
    print(seq)
    for x in base_seq:
        i0 = index[x]
        i1 = (index[x] + x) % n
        if i0 < i1:
            seq[i0:i1] = seq[i0 + 1: i1 + 1]
            seq[i1] = x
            for y in seq[i0:i1]:
                index[y] -= 1
        else:
            for y in seq[i1:i0]:
                index[y] += 1
            seq[i1 + 1:i0 + 1] = seq[i1: i0]
            seq[i1] = x

        index[x] = i1
        print(x, seq)

    print([seq[i % n] for i in range(index[0] + 1000, index[0] + 4000, 1000)])
    return sum(seq[i % n] for i in range(1000, 4000, 1000))


DATA0 = [1, 2, -3, 3, -2, 0, 4]
DATA = [x.replace('\n', '') for x in open(__file__.removesuffix('.py') + '.txt').readlines()]


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    main()
    # main(False)
