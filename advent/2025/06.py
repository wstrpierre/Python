def solve(data):
    res, buffer = 0, []
    for *vals, op in zip(*map(reversed, data.splitlines())):
        if any(map(' '.__ne__, [*vals, op])):
            buffer.append(int(''.join(vals).replace(' ', '')))
            if op != ' ':
                x = buffer[0]
                for y in buffer[1:]:
                    if op == '+':
                        x += y
                    elif op == '*':
                        x *= y
                    else:
                        raise RuntimeError(op)
                res += x
                buffer.clear()
    return res

    # Part 1
    # return sum(int(a) * int(b) * int(c) * int(d) if op == '*' else int(a) + int(b) + int(c) + int(d)
    #            for (a, b, c, d, op) in zip(*(row.split() for row in data.splitlines())))


DATA0 = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)  # 11643735527765 too low
