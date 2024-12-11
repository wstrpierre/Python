import numpy as np

T = 24

ORDERS = np.identity(4, int)

MAX_IT = 1000000

LAGS = [1, 3, 5, 3]


class Optimizer:
    def __init__(self, line):
        d = [int(x) for x in line.split(':')[1].split() if x.isnumeric()]
        self.costs = np.array(((0, d[5], 0, d[4]), (0, 0, d[3], d[2]), (0, 0, 0, d[1]), (0, 0, 0, d[0])), int)
        self.it = MAX_IT

    def search(self, t, resources, bots, orders):
        min_res = resources[0] + bots[0] * t + orders[0] * (t - 1), ()
        return max([*(self.process_order(i, t, resources, bots, orders) for i in range(4)), min_res])

    def process_order(self, i: int, t: int, resources: np.ndarray, bots: np.ndarray, orders: np.ndarray):
        if not self.it:
            return 0, ()
        self.it -= 1

        cost = self.costs[i]

        max_demand = self.costs[:, i].max() * 2
        if i > 0:
            if resources[i] >= max_demand:
                return 0, ()
            if bots[i] + orders[i] >= max_demand:
                return 0, ()

        if t == 3 and t <= LAGS[3] + cost[3]:
            return 0, ()
        if t <= LAGS[i]:
            return 0, ()

        if ((bots + orders == 0) & (cost > 0)).any():
            return 0, ()

        if (cost > resources).any():
            return self.process_order(i, t - 1, resources + bots, bots + orders, np.zeros(4, int))
        else:
            if i and (self.costs[0] <= resources).all():
                return 0, ()
            if i == 2 and (self.costs[1] <= resources).all():
                return 0, ()

            res, strat = self.search(t, resources - cost, bots, orders + ORDERS[i])
            return res, (i,) + strat

    def run(self):
        res, strat = self.search(T, np.zeros(4, int), np.array((0, 0, 0, 1), int), np.zeros(4, int))
        print(f'\n\nMax = {res} for costs:\n{self.costs}')
        print(strat)
        if self.it:
            print('Iter limit not reached.')
        else:
            print('Iter limit reached!')
        return res


def solve(data):
    return sum(Optimizer(line).run() * (i + 1) for i, line in enumerate(data))


RAW_DATA0 = '''Blueprint 1:
Each ore robot costs 4 ore.
Each clay robot costs 2 ore.
Each obsidian robot costs 3 ore and 14 clay.
Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
Each ore robot costs 2 ore.
Each clay robot costs 3 ore.
Each obsidian robot costs 3 ore and 8 clay.
Each geode robot costs 3 ore and 12 obsidian.'''

DATA0 = [part.replace('\n', ' ') for part in RAW_DATA0.split('\n\n')]
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
