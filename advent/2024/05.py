from functools import cmp_to_key


def solve(data):
    rules = [[*map(int, row.split('|'))] for row in data.split('\n\n')[0].split()]
    updates = [[*map(int, row.split(','))] for row in data.split('\n\n')[1].split()]
    order_map = {}
    for x0, x1 in rules:
        order_map.setdefault(x0, set()).add(x1)
    key = cmp_to_key(lambda x, y: (x != y) * (-1 if y in order_map.get(x, set()) else 1))
    # return sum(u1[len(u1) // 2] for u0, u1 in zip(updates, (sorted(u, key=key) for u in updates)) if u0 != u1)
    return sum(u0[len(u0) // 2] for u0, u1 in zip(updates, (sorted(u, key=key) for u in updates)) if u0 == u1)


DATA0 = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)
    # 5238
