from collections import Counter

import numpy as np
import pandas as pd
from aocd import get_data

data = get_data(year=2022, day=17)

cave = np.zeros((10000, 12), dtype=bool)
cave[-1, :] = True
cave[:, 0] = True
cave[:, 8:] = True

rocks = [
    np.array([[bool(int(x)) for x in y] for y in z.split("\n")])
    for z in [
        "0000\n0000\n0000\n1111",
        "0000\n0100\n1110\n0100",
        "0000\n0010\n0010\n1110",
        "1000\n1000\n1000\n1000",
        "0000\n0000\n1100\n1100",
    ]
]

steps = 0
for i in range(2022):
    y = np.min(np.where(np.max(cave[:, 1:8], axis=1))) - 4
    x = 3
    rock = rocks[i % 5]
    while True:
        wind = 1 if data[steps % len(data)] == ">" else -1
        steps += 1
        if not np.any(rock & cave[y - 3 : y + 1, x + wind : x + wind + 4]):
            x += wind
        if not np.any(rock & cave[y - 2 : y + 2, x : x + 4]):
            y += 1
        else:
            cave[y - 3 : y + 1, x : x + 4] |= rock
            break

out_1 = cave.shape[0] - np.min(np.where(np.max(cave[:, 1:8], axis=1))) - 1

print(out_1)

n = 10000
cave0 = np.zeros((n, 12), dtype=bool)
cave0[-1, :] = True
cave0[:, 0] = True
cave0[:, 8:] = True

cave = cave0.copy()
periods = {"counter": Counter(), "last_length": 0}
winds = [1 if d == ">" else -1 for d in data]
step = -1
i = -1
j = 0
height = 0
period_found = 0
looking_for = None
rock_diff = 0
height_diff = 0
while j < 1000000000000:
    j += 1
    i = (i + 1) % 5
    rock = rocks[i]
    y = np.min(np.where(np.max(cave[:, 1:8], axis=1))) - 4
    x = 3
    if y <= 5 or (i == 0 and period_found in [1, 3]):
        trunc_point = (
            int(pd.DataFrame(np.where(cave[:, 1:8])).T.groupby([1]).min().max())
            + 1
        )
        height += cave.shape[0] - trunc_point
        cave = np.concatenate([cave0[:-1, :], cave[:trunc_point, :]], axis=0)
        y += n - 1
        if period_found == 1:
            height_diff = height
            period_found = 2
        elif period_found == 3:
            height_diff = height - height_diff
            period_found = 4
    while True:
        step = (step + 1) % len(data)
        wind = winds[step]
        if not np.any(rock & cave[y - 3 : y + 1, x + wind : x + wind + 4]):
            x += wind
        if not np.any(rock & cave[y - 2 : y + 2, x : x + 4]):
            y += 1
        else:
            cave[y - 3 : y + 1, x : x + 4] |= rock
            if i == 0 and period_found in [0, 2]:
                if looking_for and looking_for == (step, x):
                    period_found = 3
                    rock_diff = j - rock_diff
                else:
                    periods["counter"][(step, x)] += 1
                    if periods["counter"].most_common()[0][1] > 1:
                        cur_length = len(periods["counter"].keys())
                        if periods["last_length"] == cur_length:
                            period_found = 1
                            looking_for = (step, x)
                            rock_diff = j
                        periods["last_length"] = cur_length
                        periods["counter"] = Counter()
            break
    if i == 0 and period_found == 4:
        skipping_periods = (1000000000000 - j) // rock_diff
        j += rock_diff * skipping_periods
        height += height_diff * skipping_periods
        period_found = 5

height += cave.shape[0] - np.min(np.where(np.max(cave[:, 1:8], axis=1))) - 1

print(height)
