def solve(data):
    data_map = [[*map(str.split, row[:-1].replace(',', '').split(' (contains '))] for row in data.splitlines()]
    mapped = {}
    allergens = {}

    for ing_arr, all_arr in data_map:
        for a in all_arr:
            if a in allergens:
                allergens[a] &= {*ing_arr}
            else:
                allergens[a] = {*ing_arr}

    for i in range(10):
        for a, ing_arr in allergens.items():
            if len(ing_arr) == 1:
                ing = [*ing_arr][0]
                for a0, ing_arr0 in allergens.items():
                    if a0 != a:
                        if ing in ing_arr0:
                            ing_arr0.remove(ing)

    allergens = {ing_arr.pop(): a for a, ing_arr in allergens.items()}

    # return sum(ing not in mapped for ing_arr, all_arr in data_map for ing in ing_arr)
    return ','.join(sorted(allergens, key=allergens.get))


DATA0 = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''

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
