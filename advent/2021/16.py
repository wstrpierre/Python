from scipy.constants import value

HEXA_DIGITS = '0123456789ABCDEF'
HEXA_INT_MAP = dict(zip(HEXA_DIGITS, range(len(HEXA_DIGITS))))
HEXA_MAP = {h: tuple(bool(2 ** i & x) for i in range(4))[::-1] for h, x in HEXA_INT_MAP.items()}


def to_int(bits):
    return sum(2 ** i for i, b in enumerate(bits[::-1]) if b)


def print_bits(b):
    print(''.join(map('01'.__getitem__, b)))


def decode_int(packet):
    n = packet[::5].index(False) + 1
    return to_int([b for i in range(n) for b in packet[i * 5 + 1:(i + 1) * 5]]), packet[n * 5:]


def decode_op_0(packet):
    return


def decode_op_1(packet):
    return


def decode_op(packet):
    if packet[0]:
        return decode_op_0(packet[1:])
    else:
        return decode_op_0(packet[1:])


def decode(packet):
    version, type_id = to_int(packet[:3]), to_int(packet[3:6])
    if type_id == 4:
        val = decode_int(packet[6:])
    else:
        val = decode_op(packet[6:])

    return version, val


def solve(data):
    bits = [b for c in data for b in HEXA_MAP[c]]
    value = decode(bits)
    print(value)
    return 0


# DATA0 = '''D2FE28'''
DATA0 = '''38006F45291200'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    main()
    # main(False)
