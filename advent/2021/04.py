import numpy as np


def solve(data):
    raw_seq, raw_gs = data.replace('  ', ' ').split('\n\n', 1)
    grids = np.array([[[*map(int, r.strip().split())] for r in g.split('\n')] for g in raw_gs.split('\n\n')], int)
    seq, states, wins, res = [*map(int, raw_seq.split(','))], np.zeros(grids.shape, bool), set(), 0
    for x in seq:
        states |= grids == x
        wins0 = {*np.flatnonzero((states.min(axis=1).max(axis=1) | states.min(axis=2).max(axis=1)))}
        wins0, wins = wins0 - wins, wins0
        for w in wins0:
            res = x * (~states[w] * grids[w]).sum()
    return res

DATA0 = '''7,4,9,5,11,17,23,2,0,14,21,23.txt,10,16.txt,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 23.txt
21  9 14 16.txt  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 23.txt  4
14 21 16.txt 12  6

14 21 17 23.txt  4
10 16.txt 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

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
