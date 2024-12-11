import json
from datetime import datetime, timedelta
import pandas

DATA = json.loads(open(__file__.removesuffix('.py') + '.json').read())

starts = {i: datetime(2024, 12, i, 5) for i in range(1, 26)}

data = {
    (int(day), d['name']): {
        int(part): (datetime.utcfromtimestamp(d1['get_star_ts']) - starts[int(day)]) for part, d1 in d0.items()
    }
    for d in DATA['members'].values()
    for day, d0 in d['completion_day_level'].items()
    if int(day) and d['name']
}

targets = ['Benny Hsu', 'Madeline Worley', 'Yifei Hong', 'A N', 'phongngtuan', 'Pierre Westermann', 'Bowen Yan']
data = {k0: {k1: data[k0][k1] for k1 in sorted(data[k0])} for k0 in
        sorted(data, key=lambda k: (-k[0], data[k].get(2, timedelta(days=100))))
        if len(data[k0]) == 2 and k0[1] in targets}
df = pandas.DataFrame.from_dict(data, orient='index')
# print([*DATA])
# for k, d in DATA['members']['3383168'].items():
#     print(k + '  :  ' + str(d))
#
print(df)
