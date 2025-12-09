import numpy as np


def solve(data):
    boxes = np.array([[*map(int, row.split(','))] for row in data.splitlines()], int)
    n, dim = len(boxes), len(boxes[0])
    dists = boxes * np.ones((n, n, dim), int)
    dists -= dists.transpose((1, 0, 2))
    dists = (dists ** 2).sum(axis=2)
    circuits = []
    closest = sorted((dists[i, j], i, j) for i in range(n - 1) for j in range(i + 1, n))
    remaining = {*range(n)}
    for _, *pair in closest:
        links = []
        for circuit in circuits:
            if {*pair} & circuit:
                links.append(circuit)
        if links:
            links[0] |= {*pair}
            for circuit in links[1:]:
                links[0] |= circuit
                circuits.remove(circuit)
        else:
            circuits.append({*pair})

        if len(circuits) == 1 and len(circuits[0]) == n:
            return boxes[pair[0]][0] * boxes[pair[1]][0]

    return np.prod(sorted(map(len, circuits))[-3:])
    raise ValueError('no solution')


DATA0 = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 6528 too low
