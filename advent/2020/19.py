from itertools import product
from functools import cache


def parse_rule(row):
    r_id, r = row.split(': ')
    return int(r_id), r.replace('"', '') if r[0] == '"' else [[*map(int, p.split())] for p in r.split(' | ')]


def solve(data):
    rules_raw, messages = (part.split('\n') for part in data.split('\n\n'))
    loops = {8: [[42], [42, 8]], 11: [[42, 31], [42, 11, 31]]}
    # loops = {}
    rules = dict(map(parse_rule, rules_raw)) | loops
    m = max(map(len, messages))

    @cache
    def get_rule_size(i):
        rule = rules[i]
        if isinstance(rule, str):
            return len(rule), len(rule)
        else:
            sub_sizes = [*zip(*(map(sum, zip(*[(1, m) if i == j else get_rule_size(j) for j in r])) for r in rule))]
            return min(sub_sizes[0]), max(sub_sizes[1])

    def match_rule(expr, rule):
        if isinstance(rule, str):
            return expr == rule
        else:
            for i in rule:
                s = get_rule_size(i)[0]
                if match(expr[:s], i):
                    expr = expr[s:]
                else:
                    return False
            return True

    def match(expr, i=0):
        s = get_rule_size(i)
        if s[0]<=len(expr)<=s[1]:
            return any(match_rule(expr, rule) for rule in rules[i])

    s = get_rule_size(0)
    for _i in rules:
        print(f'{_i} => {get_rule_size(_i)}')

    x = 0
    return 0


DATA0 = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''

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
