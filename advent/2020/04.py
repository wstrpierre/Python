FLDS = {'ecl', 'eyr', 'hcl', 'byr', 'iyr', 'hgt', 'pid'}


def is_valid(d):
    data = dict(fld.split(':') for fld in d.split())
    if FLDS - {*data}:
        return False
    for fld, x0, x1 in [('byr', 1920, 2002), ('iyr', 2010, 2020), ('eyr', 2020, 2030)]:
        if not (len(data[fld]) == 4 and x0 <= int(data[fld]) <= x1):
            return False
    if not data['hgt'].endswith(('cm','in')):
        return False
    x0, x1 = {'cm': (150, 193), 'in': (59, 76)}[data['hgt'][-2:]]
    if not x0 <= int(data['hgt'][:-2]) <= x1:
        return False
    if not (data['hcl'][0] == '#' and len(data['hcl']) == 7 and all(c in '0123456789abcdef' for c in data['hcl'][1:])):
        return False
    if not data['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False
    if not (len(data['pid']) == 9 and all(c.isdigit() for c in data['pid'])):
        return False
    return True


def solve(data):
    return sum(map(is_valid, data.split('\n\n')))


DATA0 = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

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
