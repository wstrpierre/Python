from time import time_ns


def parse_line(line):
    ends = sorted(tuple(map(int, x.split(','))) for x in line.split('~'))
    diffs = [x1 - x0 for x0, x1 in zip(*ends)]
    size = max(diffs)
    return ends[0][-1], ends[0][:-1], size + 1, diffs.index(size)


def solve(data):
    bricks = [b[1:] for b in sorted(map(parse_line, data))]

    print('\n'.join(f'{xy}: {size} => {orient}' for xy, size, orient in bricks))

    grid, block_map, support_map, dep_map = {}, {}, {}, {}
    for b, (xy, size, orient) in enumerate(bricks):
        if orient == 2:
            proj, h = [xy], size
        else:
            proj, h = [tuple(x + i * (k == orient) for k, x in enumerate(xy)) for i in range(size)], 1
        z0 = max(grid.get(p, 0) for p in proj)
        z = z0 + h
        blocks = [(*p, z) for p in proj]
        block_map |= {xyz: b for xyz in blocks}
        grid |= {p: z for p in proj}
        supports = {block_map[x, y, z0] for x, y, z in blocks if (x, y, z0) in block_map}
        dep_map[b] = supports
        for b0 in supports:
            support_map.setdefault(b0, set()).add(b)

    def list_falls(ids):
        deps = {b for b0 in ids for b in support_map.get(b0, set())} - ids
        new_falls = {b for b in deps if not dep_map[b] - ids}
        if new_falls:
            return list_falls(ids | new_falls)
        else:
            return ids

    return sum(len(list_falls({b})) - 1 for b in range(len(bricks)))


DATA0 = ['1,0,1~1,2,1', '0,0,2~2,0,2', '0,2,3~2,2,3', '0,0,4~0,2,4', '2,0,5~2,2,5', '0,1,6~2,1,6', '1,1,8~1,1,9']
DATA = open(__file__.removesuffix('.py') + '.txt').readlines()

t0 = time_ns()
solution = solve(DATA)
calc_time = (time_ns() - t0) / 1e6

print(f'Solution ====> {solution:.0f} | Calc time = {calc_time} ms.')
