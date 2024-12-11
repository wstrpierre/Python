K = 3


def parse_network(data):
    raw_net = {line.split(': ')[0]: line.split(': ')[1].split() for line in data}
    node_names = sorted({*raw_net} | {dep for deps in raw_net.values() for dep in deps})
    id_map = {name: i for i, name in enumerate(node_names)}
    network = {}

    for name, deps in raw_net.items():
        for dep in deps:
            network.setdefault(id_map[name], {})[id_map[dep]] = 1
            network.setdefault(id_map[dep], {})[id_map[name]] = 1

    return network


def _find_path(network, target, flows, current, visited):
    if current:
        if target in current:
            return [target]
        else:
            current1 = {x1 for x0 in current for x1, w in network[x0].items() if w > flows.get((x0, x1), 0)}
            visited |= current
            current1 -= visited
            path = _find_path(network, target, flows, current1, visited)
            if path:
                y1 = path[0]
                y0 = next(y for y, w in network[y1].items() if y in current and flows.get((y, y1), 0) < w)
                return [y0, *path]
            else:
                return []
    else:
        return []


def find_path(network, start, target, flows=None):
    return _find_path(network, target, flows or {}, {start}, set())


def get_path_edges(path):
    return [*zip(path[:-1], path[1:]), *zip(path[1:], path[:-1])]


def add_dict(*args):
    return {k: sum(flows.get(k, 0) for flows in args) for k in {k for flows in args for k in flows}}


def _get_all_paths(network, x0, x1, depth, flows):
    if not depth:
        return []
    path = find_path(network, x0, x1, flows)
    if path:
        flows = add_dict(flows, {edge: 1 for edge in get_path_edges(path)})
        return [path, *_get_all_paths(network, x0, x1, depth - 1, flows)]
    else:
        return []


def get_all_paths(network, x0, x1, depth=K + 1):
    return _get_all_paths(network, x0, x1, depth, {})


def merge_nodes(network, nodes):
    if len(nodes) < 2:
        return network
    elif len(nodes) == 2:
        x0, x1 = sorted(nodes)
        del network[x0][x1]
        del network[x1][x0]
        for x, flow in network[x1].items():
            network[x0][x] = network[x][x0] = flow + network[x0].get(x, 0)
            if x == x1:
                print(nodes)
            del network[x][x1]
        del network[x1]
    else:
        nodes0, nodes1 = nodes[:len(nodes) // 2], nodes[len(nodes) // 2:]
        merge_nodes(network, nodes0)
        merge_nodes(network, nodes1)
        merge_nodes(network, [min(nodes0), min(nodes1)])


def get_distances(network, x0=0):
    pending, dists, i = {x0}, {}, 0
    while pending:
        dists |= {x: i for x in pending}
        pending = {x1 for x in pending for x1 in network[x] if x1 not in dists}
        i += 1
    return dists


def solve(data):
    network = parse_network(data)
    size = len(network)
    dists0 = get_distances(network)
    x0 = max(dists0, key=dists0.get)
    dists = get_distances(network, x0)
    x1 = max(dists, key=dists.get)
    paths = get_all_paths(network, x0, x1)
    while len(paths) > K:
        merge_nodes(network, (x1, x0))
        x0 = min(x1, x0)
        dists = get_distances(network, x0)
        x1 = max(dists, key=dists.get)
        paths = get_all_paths(network, x0, x1)

    cuts, paths = [], [path[1:] for path in paths]
    for path in paths:
        while len(path) > 1:
            x1 = path[0]
            sub_paths = get_all_paths(network, x0, x1)
            if len(sub_paths) > K:
                merge_nodes(network, (x0, x1))
                x0 = min(x0, x1)
                path.pop(0)
            else:
                path = path[:1]
        cuts.append(path[0])

    for x1 in cuts:
        del network[x0][x1]
        del network[x1][x0]

    pending, nodes = {cuts[0]}, set()

    while pending:
        nodes |= pending
        pending = {x1 for x0 in pending for x1 in network[x0] if x1 not in nodes}

    return len(nodes) * (size - len(nodes))


DATA = [x.replace('\n', '') for x in open(__file__.removesuffix('.py') + '.txt').readlines()]

DATA0 = ['jqt: rhn xhk nvd', 'rsh: frs pzl lsr', 'xhk: hfx', 'cmg: qnr nvd lhk bvb', 'rhn: xhk bvb hfx',
         'bvb: xhk hfx', 'pzl: lsr hfx nvd', 'qnr: nvd', 'ntq: jqt hfx bvb xhk', 'nvd: lhk', 'lsr: lhk',
         'rzs: qnr cmg lsr rsh', 'frs: qnr lhk lsr']


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution:.0f} | Calc time = {calc_time} ms.')


if __name__ == '__main__':
    # main()
    main(False)
