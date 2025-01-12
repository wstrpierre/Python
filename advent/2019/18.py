import numpy as np
from scipy.ndimage import convolve
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import coo_matrix
from heapq import heappop, heappush


def solve(data):
    raw = np.array([[*row] for row in data.split()], 'U1')

    grid, id_map, w = raw != '#', np.arange(raw.size).reshape(raw.shape), raw.shape[1]
    nbs, ids, msk = convolve(grid, [[0, 1, 0], [2, 0, 8], [0, 4, 0]], int)[grid], id_map[grid], raw >= '@'
    gen, nodes = ((s, ids[nbs & 2 ** k > 0]) for k, s in enumerate([w, 1, -w, -1])), dict(zip(raw[msk], id_map[msk]))
    edges, nodes = np.concatenate([np.stack((nb_ids, nb_ids + s)).T for s, nb_ids in gen]), dict(sorted(nodes.items()))
    m, nids = tuple(np.where(np.isin(edges[:, 1], [*nodes.values()]))[0]), {k: i for i, k in enumerate(nodes.values())}
    edges[m, 1], nmap, n = [*map(nids.get, edges[m, 1])], [*nodes], sum(map(str.islower, nodes))
    dists = dijkstra(coo_matrix((np.ones(len(edges)), edges.T)), True, [*nids])[:, [*nids.values()]]
    net = {nmap[i]: {nmap[j]: d for j, d in enumerate(r) if i != j and 0 < d < 1e4} for i, r in enumerate(dists)}
    pending, visited, res, tgt = [(0, '@', 0)], {}, 1e6, 2 ** n - 1

    while pending:
        d0, head, seq = heappop(pending)
        if d0 < visited.get((head, seq), res):
            visited[head, seq] = d0
            if seq == tgt:
                res = d0
            else:
                for k, d1 in net[head].items():
                    if k.isupper():
                        if (seq >> (ord(k) - 65)) & 1 and d0 + d1 < visited.get((k, seq), 1e6):
                            heappush(pending, (d0 + d1, k, seq))
                    elif k.islower():
                        seq1 = seq | (1 << (ord(k) - 97))
                        if d0 + d1 < visited.get((k, seq1), 1e6):
                            heappush(pending, (d0 + d1, k, seq1))
                    else:
                        if d0 + d1 < visited.get((k, seq), 1e6):
                            heappush(pending, (d0 + d1, k, seq))

    return res


DATA0 = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.3f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 2684
