import numpy as np
from scipy.ndimage import convolve
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import coo_matrix


def get_net(raw):
    id_map, grid = 56 + np.arange(raw.size).reshape(raw.shape), raw != '#'
    neighbors = convolve(raw != '#', [[0, 1, 0], [2, 0, 8], [0, 4, 0]], int)[raw != '#']
    ids, width, keys, m = id_map[grid], grid.shape[1], ''.join(sorted(raw[raw >= 'a'])), id_map.max()
    gen_edges = ((s, ids[neighbors & 2 ** k > 0]) for k, s in enumerate([width, 1, -width, -1]))
    edges = np.concatenate([np.stack((nb_ids, nb_ids + s)).T for s, nb_ids in gen_edges])
    nodes, node_ids = raw[raw > '.'], id_map[raw > '.']
    edge_mask, n = tuple(np.where(np.isin(edges[:, 1], node_ids))[0]), len(nodes)
    edges[edge_mask, 1] = [*map(dict(zip(node_ids, range(n))).get, edges[edge_mask, 1])]
    dists = dijkstra(coo_matrix((np.ones(len(edges)), edges.T), (m, m)), True, node_ids)[:, range(n)]
    return {i: {j: int(x) for j, x in zip(nodes, d) if i != j and x < 1e9} for i, d in zip(nodes, dists)}, keys


def solve_1(data):
    queues, seen, (net, tgt) = [[('@', '')]], set(), get_net(np.array([*map(list, data.split())]))
    for t, queue in enumerate(queues):
        for head, keys in queue:
            keys = ''.join(sorted(keys + head)) if head.islower() and head not in keys else keys
            if keys == tgt:
                return t
            if (head, keys) not in seen:
                seen.add((head, keys))
                for h, dt in net[head].items():
                    if not h.isupper() or h.lower() in keys:
                        while len(queues) <= t + dt:
                            queues.append([])
                        queues[t + dt].append((h, keys))


def solve_2(data):
    raw = np.array([[*row] for row in data.split()])

    starts = np.argwhere(raw == '@')
    if len(starts) > 1:
        raw[tuple(starts.T)] = range(len(starts))
    else:
        i, j = starts[0]
        raw[i - 1:i + 2, j - 1:j + 2] = ('0', '#', '1'), ('#', '#', '#'), ('2', '#', '3')

    queues, seen, (net, tgt) = [[('0123', '')]], set(), get_net(raw)
    for t, queue in enumerate(queues):
        for heads, keys in queue:
            for head in heads:
                if keys == tgt:
                    return t
                if (head, keys) not in seen:
                    seen.add((head, keys))
                    for h, dt in net[head].items():
                        keys1 = ''.join(sorted(keys + h)) if h.islower() and h not in keys else keys
                        if not h.isupper() or h.lower() in keys1:
                            while len(queues) <= t + dt:
                                queues.append([])
                            queues[t + dt].append((heads.replace(head, h), keys1))


def solve(data):
    return solve_1(data), solve_2(data)


DATA1 = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''

DATA2 = '''#############
#DcBa.#.GhKl#
#.###@#@#I###
#e#d#####j#k#
###C#@#@###J#
#fEbA.#.FgHi#
#############'''

DATA0 = DATA2
DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.3f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 2684 | 1886
