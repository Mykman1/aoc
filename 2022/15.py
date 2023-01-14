import re

import numpy as np
from aocd import get_data

data = get_data(year=2022, day=15)
inp = [
    {"s": (int(y[0]), int(y[1])), "b": (int(y[2]), int(y[3]))}
    for y in [
        re.search(
            r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$",
            x,
        ).groups()
        for x in data.split("\n")
    ]
]

for r in inp:
    r["d"] = abs(r["s"][0] - r["b"][0]) + abs(r["s"][1] - r["b"][1])

max_x = max([x["s"][0] for x in inp]) + max([x["d"] for x in inp])
min_x = min([x["s"][0] for x in inp]) - max([x["d"] for x in inp])

row = np.zeros(max_x - min_x + 1, dtype=bool)
fixed_y = 2000000

for r in inp:
    dist = r["d"] - abs(r["s"][1] - fixed_y)
    if dist >= 0:
        row[r["s"][0] - min_x - dist : r["s"][0] - min_x + dist + 1] = True

for r in inp:
    if r["s"][1] == fixed_y:
        row[r["s"][0] - min_x] = False
    if r["b"][1] == fixed_y:
        row[r["b"][0] - min_x] = False

out_1 = np.sum(row)

print(out_1)

search_range = 4000000

for r in inp:
    start_dirs = [
        ((r["s"][0] - r["d"] - 1, r["s"][1]), (1, -1)),
        ((r["s"][0], r["s"][1] - r["d"] - 1), (1, 1)),
        ((r["s"][0] + r["d"] + 1, r["s"][1]), (-1, 1)),
        ((r["s"][0], r["s"][1] + r["d"] + 1), (-1, -1)),
    ]
    for sp, dr in start_dirs:
        for i in range(r["d"] + 1):
            x, y = sp[0] + i * dr[0], sp[1] + i * dr[1]
            if not ((0 <= x <= search_range) and (0 <= y <= search_range)):
                continue
            found = True
            for r2 in inp:
                if abs(r2["s"][0] - x) + abs(r2["s"][1] - y) <= r2["d"]:
                    found = False
                    break
            if found:
                found = x, y
                break
        if found:
            break
    if found:
        break

out_2 = 4000000 * found[0] + found[1]

print(out_2)
