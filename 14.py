from collections import Counter

from aocd import get_data

data = get_data(day=14)

inp, maps = data.split("\n\n")
maps = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in maps.split("\n")}

polys = inp
for i in range(10):
    inserts = [maps["".join([x, y])] for x, y in zip(polys[:-1], polys[1:])] + [
        ""
    ]
    polys = "".join([y for x in zip(polys, inserts) for y in x])

cnt = Counter(polys)

print(cnt.most_common()[0][1] - cnt.most_common()[-1][1])


polys = inp
count_maps = {k: [k[0] + v, v + k[1]] for k, v in maps.items()}

cnt_comb = Counter()
for x, y in zip(polys[:-1], polys[1:]):
    cnt_comb[x + y] += 1

for i in range(40):
    cnt_comb_new = Counter()
    for j in cnt_comb.keys():
        for k in count_maps[j]:
            cnt_comb_new[k] += cnt_comb[j]
    cnt_comb = cnt_comb_new

cnt = Counter()

for k in cnt_comb.keys():
    for c in k:
        cnt[c] += cnt_comb[k]

first_char = inp[0]
last_char = inp[-1]

cnt[first_char] += 1
cnt[last_char] += 1

print((cnt.most_common()[0][1] // 2) - (cnt.most_common()[-1][1] // 2))
