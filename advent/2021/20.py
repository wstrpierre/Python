import numpy as np

N = 50


def solve(data):
    str_algo, str_pic = data.split('\n\n')
    algo, pic = [*map('#'.__eq__, str_algo)], np.array([[*map('#'.__eq__, row)] for row in str_pic.split('\n')], int)

    print('\n')
    print('\n'.join(''.join(map(' #'.__getitem__, row)) for row in pic))
    fill = 0
    for t in range(N):
        frame, fill = np.ones((pic.shape[0] + 4, pic.shape[1] + 4), int) * fill, algo[-fill]
        frame[2:-2, 2:-2], pic = pic, np.zeros((pic.shape[0] + 2, pic.shape[1] + 2), int)
        for i in range(1, frame.shape[0] - 1):
            for j in range(1, frame.shape[1] - 1):
                part = frame[i - 1: i + 2, j - 1: j + 2]
                z = sum(x * 2 ** k for k, x in enumerate(part.flat[::-1]))
                # print(f'\n{i} {j} => {z} ({int(algo[z])})\n{part * 1}')
                pic[i - 1, j - 1] = algo[z]
        # print(f'\n====> TRANSFORM {t}\n ')
        # print('\n'.join(''.join(map(' #'.__getitem__, row)) for row in pic))
    print('\n'.join(''.join(map(' #'.__getitem__, row)) for row in pic))
    return pic.sum()


DATA0 = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 5402 too high
