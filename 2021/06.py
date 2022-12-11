from collections import Counter

from aocd import get_data

data = get_data(day=6)
inp = [int(x) for x in data.split(",")]

cnt = Counter(inp)

for i in range(80):
    c0 = cnt[0]
    cnt_new = Counter()
    for k in range(1, 10):
        cnt_new[k - 1] = cnt[k]
    cnt_new[8] += c0
    cnt_new[6] += c0
    cnt = cnt_new

print(sum([v for k, v in cnt.items()]))

cnt = Counter(inp)

for i in range(256):
    c0 = cnt[0]
    cnt_new = Counter()
    for k in range(1, 10):
        cnt_new[k - 1] = cnt[k]
    cnt_new[8] += c0
    cnt_new[6] += c0
    cnt = cnt_new

print(sum([v for k, v in cnt.items()]))
