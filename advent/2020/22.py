
def play(hands):
    print(f'Playing game:')
    print('\n'.join('\t' + ' '.join(map('{:02}'.format, hand)) for hand in hands))
    loop = set()
    while all(hands):
        key = tuple(map(tuple, hands))
        if key in loop:
            print(f'Loop found.')
            return 0
        else:
            loop.add(key)
        cards = [hand.pop(0) for hand in hands]

        # w = cards.index(max(cards))
        if any(card > len(hand) for card, hand in zip(cards, hands)):
            w = cards.index(max(cards))
        else:
            print('Sub game on ' + ' '.join(map('{:02}'.format, cards)))
            # if max(hands[0]) > max(hands[1]) and max(hands[0]) > sum(map(len, hands)) - 2:
            #     print('Shortcut found.')
            #     print('\n'.join('\t\t' + ' '.join(map('{:02}'.format, hand)) for hand in hands))
            #     # return 0
            #     w = 0
            # else:
            w = play([hand[:card] for card, hand in zip(cards, hands)])

        hands[w] += [cards[w], cards[1 - w]]
    winner = next(i for i, hand in enumerate(hands) if hand)
    print(f'Player {winner + 1} wins!')
    return winner


def solve(data):
    hands = [[*map(int, raw_hand.splitlines()[1:])] for raw_hand in data.split('\n\n')]
    # hands =hands[::-1]
    winner = play(hands)
    final_hand = hands[winner]
    print('\n\nFinal Hand: ' + ' '.join(map('{:02}'.format, final_hand)))
    return sum(i * c for i, c in enumerate(reversed(final_hand), 1))


DATA0 = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main() # 306
    main(False)  # 32629 | 36739 too high
