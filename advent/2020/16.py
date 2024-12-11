from cProfile import runctx

import numpy as np
from numpy.linalg import inv
from math import prod


def solve(data):
    str_rules, str_ticket, str_nearby = [part.split('\n') for part in data.split('\n\n')]
    rules = {k: [[*map(int, rng.split('-'))] for rng in rule.split(' or ')]
             for k, rule in (row.split(': ') for row in str_rules)}
    ticket = [*map(int, str_ticket[1].split(','))]
    nearby = np.array([[*map(int, row.split(','))] for row in str_nearby[1:]], int)
    check = np.array([((nearby >= x00) & (nearby <= x01) | (nearby >= x10) & (nearby <= x11))
                      for (x00, x01), (x10, x11) in rules.values()])
    key_map = np.where(inv(check[:, check.any(0).all(1), :].all(1)).T == 1)[1]
    return prod(ticket[key_map[i]] for i, k in enumerate(rules) if k.split()[0] == 'departure')


DATA0 = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 183706337483 too low
