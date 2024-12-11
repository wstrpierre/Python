def is_solved(slots):
    return all(s == i for i, slot in enumerate(slots) for s in slot)


def next_states(slots, hallway):
    def get_dist(i, j):
        path = hallway[i + 1:2 + j] if i < 3 + j else hallway[3 + j:i]
        d = (len(path) + 1) * 2 - (i in (0, 6)) + sum(s < 0 for s in slots[j])
        return d if all(x < 0 for x in path) else 0

    def next_states_hallway():
        for i, h in enumerate(hallway):
            if h >= 0 and all(s in (-1, h) for s in slots[h]) and (d := get_dist(i, h)):
                slots0 = [(h, -1 if slot[0] < 0 else h) if h == j else slot for j, slot in enumerate(slots)]
                hallway0 = [-1 if i0 == i else h0 for i0, h0 in enumerate(hallway)]
                # print(h, slots0)
                yield (tuple(slots0), tuple(hallway0)), d * 10 ** h

    def next_states_slots():
        for j, slot in enumerate(slots):
            s = slot[slot[1] >= 0]
            if s >= 0 and (s != j or slot[0] != j):
                for i, h in enumerate(hallway):
                    if h < 0 and (d := get_dist(i, j)):
                        slots0 = [(-1 if slot[1] < 0 else slot[0], -1) if j == j0 else slot0
                                  for j0, slot0 in enumerate(slots)]
                        hallway0 = [s if i0 == i else h0 for i0, h0 in enumerate(hallway)]
                        yield (tuple(slots0), tuple(hallway0)), d * 10 ** s

    res = [*next_states_hallway(), *next_states_slots()]

    if not res:
        print(slots, hallway)
    return res


def solve(data):
    states = {(data, (-1,) * 7): 0}
    best = int(1e9)
    print(data)
    for _ in range(1000000):
        state0, energy0 = states.popitem()
        # print(state0)
        for state, energy in next_states(*state0):
            if is_solved(state[0]):
                best = min(energy0 + energy, best)
            else:
                states[state] = energy0 + energy
    return best


DATA0 = (0, 1), (3, 2), (2, 1), (0, 3)
DATA = (3, 0), (0, 2), (3, 1), (1, 2)


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    main()
    # main(False)
