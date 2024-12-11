from functools import cache

T = 30
S = 'AA'
E = 4


def parse_row(row: str):
    parts = row.split('; ')
    v_id, flow = parts[0].split()[1], int(parts[0].split('=')[-1])
    v_ids = tuple(parts[1].split(' ', 4)[-1].split(', '))
    return v_id, (flow, v_ids)


def solve(data):
    valves_data = dict(map(parse_row, data))
    n, m = len(valves_data), sum(flow > 0 for flow, _ in valves_data.values())
    valves = sorted(valves_data, key=valves_data.get, reverse=True)
    id_map = {v_id: i for i, v_id in enumerate(valves)}
    network = [tuple(sorted(map(id_map.get, valves_data[v_id][1]))) for v_id in valves]
    flows = [valves_data[v_id][0] for v_id in valves]

    def get_dists(i):
        res, pending, d = [-1] * n, {i}, 0
        while pending:
            for j in pending:
                res[j] = d
            pending = {j0 for j in pending for j0 in network[j] if res[j0] < 0}
            d += 1
        return res

    dists = [get_dists(i) for i in range(n)]

    @cache
    def search(i, t, pending):
        t -= 1
        pending = tuple(i0 for i0 in pending if i0 != i and t - dists[i][i0] - 1 > 1)
        return flows[i] * t + max((search(i0, t - dists[i][i0], pending) for i0 in pending), default=0)

    strats = [(tuple(i for i in range(m) if 2 ** i & k), tuple(i for i in range(m) if not 2 ** i & k))
              for k in range(2 ** m)]

    # return search(id_map[S], T + 1, tuple(range(m)))
    return max(sum(search(id_map[S], T - 3, grp) for grp in groups) for groups in strats)


DATA0 = ['Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
         'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
         'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
         'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
         'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
         'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
         'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
         'Valve HH has flow rate=22; tunnel leads to valve GG',
         'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
         'Valve JJ has flow rate=21; tunnel leads to valve II']

DATA = [x.replace('\n', '') for x in open(__file__.removesuffix('.py') + '.txt').readlines()]


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)
