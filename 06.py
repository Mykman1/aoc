from collections import Counter

from aocd import get_data

data = get_data(day=6)
in_1 = [int(x) for x in data.split(",")]

cnt = Counter(in_1)

for i in range(80):
    c0 = cnt[0]
    cnt_new = Counter()
    for k in range(1, 10):
        cnt_new[k - 1] = cnt[k]
    cnt_new[8] += c0
    cnt_new[6] += c0
    cnt = cnt_new

print(sum([v for k, v in cnt.items()]))

in_2 = in_1

cnt = Counter(in_2)

for i in range(256):
    c0 = cnt[0]
    cnt_new = Counter()
    for k in range(1, 10):
        cnt_new[k - 1] = cnt[k]
    cnt_new[8] += c0
    cnt_new[6] += c0
    cnt = cnt_new

print(sum([v for k, v in cnt.items()]))
