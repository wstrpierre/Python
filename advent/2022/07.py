MAX_MEM = 70000000
REQ_MEM = 30000000


def get_tree(commands):
    tree = {}
    path, curr_dir = [], tree
    in_list = False
    for cmd in commands:
        if cmd.startswith('$ '):
            cmd = cmd.removeprefix('$ ')
            if cmd == 'ls':
                in_list = True
            else:
                in_list = False
                if cmd.startswith('cd '):
                    cmd = cmd.removeprefix('cd ')
                    if cmd == '/':
                        path, curr_dir = [], tree
                    elif cmd == '..':
                        curr_dir = path.pop()
                    else:
                        path.append(curr_dir)
                        curr_dir = curr_dir[cmd]
                else:
                    raise ValueError(f'Unknown command: {cmd}')
        else:
            if in_list:
                c0, name = cmd.split()
                if c0 == 'dir':
                    curr_dir.setdefault(name, {})
                else:
                    curr_dir[name] = int(c0)
            else:
                ValueError('No command and no list')
    return tree


def get_size_tree(tree):
    size = 0
    size_tree = {}
    for name, o in tree.items():
        if isinstance(o, int):
            size += o
        else:
            sub_tree = get_size_tree(o)
            size += sub_tree[()]
            size_tree |= {(name, *path): o1 for path, o1 in sub_tree.items()}
    size_tree[()] = size
    return size_tree


def solve(data):
    tree = get_tree(data)

    size_tree = get_size_tree(tree)
    total_size = size_tree[()]
    return min(size for size in size_tree.values() if size >= total_size + REQ_MEM - MAX_MEM)


DATA0 = ['$ cd /', '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e', '29116 f',
         '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j',
         '8033020 d.log', '5626152 d.ext', '7214296 k']

DATA = [x.replace('\n', '') for x in open(__file__.removesuffix('.py') + '.txt').readlines()]


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6

    print(f'Solution ====> {solution} | Calc time = {calc_time} ms.')


if __name__ == '__main__':
    # main()
    main(False)
