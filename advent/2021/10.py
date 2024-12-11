BRACKETS, SCORES = '()[]{}<>', (3, 57, 1197, 25137)


def get_score(seq):
    state = []
    for x in map(BRACKETS.index, seq):
        if x % 2:
            if state[-1] == x // 2:
                del state[-1]
            else:
                return 0
        else:
            state.append(x // 2)
    return sum((x + 1) * 5 ** i for i, x in enumerate(state))


def solve(data):
    scores = sorted(score for score in map(get_score, data.split()) if score)
    return scores[len(scores) // 2]


DATA0 = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

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
