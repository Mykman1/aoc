from collections import Counter

from aocd import get_data

data = get_data(day=7)
inp = [int(x) for x in data.split(",")]

cnt = Counter()
for i in range(min(inp), max(inp) + 1):
    for j in range(len(inp)):
        cnt[i] += abs(inp[j] - i)

print(cnt.most_common()[-1][1])

cnt = Counter()
for i in range(min(inp), max(inp) + 1):
    for j in range(len(inp)):
        cnt[i] += (abs(inp[j] - i) * (abs(inp[j] - i) + 1)) // 2

print(cnt.most_common()[-1][1])
