LIMIT = {'red': 12, 'green': 13, 'blue': 14}


def get_score(row):
    str_game_id, str_games = row.split(': ')
    for str_game in str_games.split('; '):
        for part in str_game.split(', '):
            if int(part.split()[0]) > LIMIT[part.split()[1]]:
                return 0
    return int(str_game_id.split(' ')[1])


def solve(data):
    return sum(map(get_score, data.split('\n')))


DATA0 = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

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
