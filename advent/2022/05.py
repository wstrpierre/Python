def solve(data):
    s = data.index('')
    stack_data, n = [line[1::4] for line in data[s - 2::-1]], max(map(int, data[s - 1].split()))
    cmd = [tuple(map(int, line.split()[1::2])) for line in data[s + 1:]]
    stacks = [[line[i] for line in stack_data if line[i] != ' '] for i in range(n)]

    for n, i, j in cmd:
        stacks[j - 1] += stacks[i - 1][-n:]
        stacks[i - 1] = stacks[i - 1][:-n]

    return ''.join(stack[-1] for stack in stacks)


DATA0 = ['    [D]    ',
         '[N] [C]    ',
         '[Z] [M] [P]',
         ' 1   2   3 ',
         '',
         'move 1 from 2 to 1',
         'move 3 from 1 to 3',
         'move 2 from 2 to 1',
         'move 1 from 1 to 2']

DATA = [x.replace('\n', '') for x in open(__file__.removesuffix('.py') + '.txt').readlines()]


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6

    print(f'Solution ====> {solution} | Calc time = {calc_time} ms.')


if __name__ == '__main__':
    main(False)
