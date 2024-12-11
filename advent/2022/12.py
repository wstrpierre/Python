def solve(data):
    start = next((i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == 'S')
    end = next((i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == 'E')
    grid = [[ord(c.replace('S', 'a').replace('E', 'z')) - ord('a') for c in row] for row in data]
    max_i, max_j = len(data), len(data[0])

    def get_neighbours(i0, j0):
        return [(i, j) for i, j in [(i0 - 1, j0), (i0 + 1, j0), (i0, j0 - 1), (i0, j0 + 1)]
                if 0 <= i < max_i and 0 <= j < max_j and grid[i][j] + 1 >= grid[i0][j0]]

    visited, pending, n = set(), {end}, 0
    while all(grid[i][j] for i, j in pending):
        n += 1
        visited |= pending
        pending = {p for p0 in pending for p in get_neighbours(*p0)} - visited

    return n


DATA0 = ['Sabqponm', 'abcryxxl', 'accszExk', 'acctuvwj', 'abdefghi']

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
