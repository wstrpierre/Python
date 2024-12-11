from math import prod


def seq_score(seq, k, step):
    score = 0
    for x in seq[k + step::step]:
        score += 1
        if x >= seq[k]:
            return score
    return score


def solve(data):
    rows, n = [[*map(int, line)] for line in data], len(data)
    cols = [[rows[i][j] for i in range(n)] for j in range(n)]

    def get_tree_score(i, j):
        return prod(seq_score(seq, k, step) for seq, k in ((rows[i], j), (cols[j], i)) for step in (-1, 1))

    return max(get_tree_score(i, j) for i in range(1, n - 1) for j in range(1, n - 1))


DATA0 = ['30373', '25512', '65332', '33549', '35390']

DATA = [x.replace('\n', '') for x in open(__file__.removesuffix('.py') + '.txt').readlines()]


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6

    print(f'Solution ====> {solution} | Calc time = {calc_time} ms.')


if __name__ == '__main__':
    # main()
    main(False)
