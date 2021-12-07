from collections import Counter

from aocd import get_data

data = get_data(day=7)
in_1 = [int(x) for x in data.split(",")]

cnt = Counter()
for i in range(min(in_1), max(in_1) + 1):
    for j in range(len(in_1)):
        cnt[i] += abs(in_1[j] - i)

print(cnt.most_common()[-1][1])

in_2 = in_1

cnt = Counter()
for i in range(min(in_2), max(in_2) + 1):
    for j in range(len(in_2)):
        cnt[i] += (abs(in_2[j] - i) * (abs(in_2[j] - i) + 1)) // 2

print(cnt.most_common()[-1][1])
