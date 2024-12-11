class Vect(tuple):
    def __add__(self, v):
        return Vect(map(sum, zip(self, v)))

    def __rmul__(self, k):
        return Vect(map(k.__mul__, self))

    def __sub__(self, v):
        return self + -1 * v

    def __abs__(self):
        return Vect(map(abs, self))


DIRS = {d: Vect(x) for d, x in zip('UDLR', ((1, 0), (-1, 0), (0, -1), (0, 1)))}


def solve(data):
    moves = [(DIRS[line[0]], int(line[2:])) for line in data]
    n = 10
    rope = [Vect((0, 0))] * n
    tails = {rope[-1]}

    for m, k in moves:
        for _ in range(k):
            rope[0] += m
            for i in range(1, n):
                dist = rope[i - 1] - rope[i]
                if max(abs(dist)) > 1:
                    rope[i] += Vect(min(max(x, -1), 1) for x in dist)
            tails.add(rope[-1])
    return len(tails)


# DATA0 = ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']
DATA0 = ['R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']
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
