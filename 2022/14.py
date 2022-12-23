import numpy as np
from aocd import get_data

data = get_data(year=2022, day=14)

inp = [
    list(zip(t[:-1], t[1:]))
    for t in [
        [tuple([int(z) for z in y.split(",")]) for y in x.split(" -> ")]
        for x in data.split("\n")
    ]
]

max_y = max([z[1] for x in inp for y in x for z in y])
min_x = min([z[0] for x in inp for y in x for z in y])
max_x = max([z[0] for x in inp for y in x for z in y])

cave_1 = np.zeros((max_y + 2, max_x - min_x + 3), dtype=bool)
for path in inp:
    for p1, p2 in path:
        p1, p2 = (min(p1[0], p2[0]) - min_x + 1, min(p1[1], p2[1])), (
            max(p1[0], p2[0]) - min_x + 1,
            max(p1[1], p2[1]),
        )
        cave_1[p1[1] : p2[1] + 1, p1[0] : p2[0] + 1] = True

stop = False
out_1 = 0
while not stop:
    pos = [501 - min_x, 0]
    while True:
        if pos[1] > max_y:
            stop = True
            break
        elif not cave_1[pos[1] + 1, pos[0]]:
            pos[1] += 1
        elif not cave_1[pos[1] + 1, pos[0] - 1]:
            pos[0] -= 1
            pos[1] += 1
        elif not cave_1[pos[1] + 1, pos[0] + 1]:
            pos[0] += 1
            pos[1] += 1
        else:
            cave_1[pos[1], pos[0]] = True
            out_1 += 1
            break

print(out_1)

min_x = min(min_x, 497 - max_y)
max_x = max(max_x, 503 + max_y)
cave_2 = np.zeros((max_y + 3, max_x - min_x + 3), dtype=bool)
for path in inp:
    for p1, p2 in path:
        p1, p2 = (min(p1[0], p2[0]) - min_x + 3, min(p1[1], p2[1])), (
            max(p1[0], p2[0]) - min_x + 3,
            max(p1[1], p2[1]),
        )
        cave_2[p1[1] : p2[1] + 1, p1[0] : p2[0] + 1] = True
cave_2[-1, :] = True

stop = False
out_2 = 0
while not stop:
    pos = [503 - min_x, 0]
    while True:
        if not cave_2[pos[1] + 1, pos[0]]:
            pos[1] += 1
        elif not cave_2[pos[1] + 1, pos[0] - 1]:
            pos[0] -= 1
            pos[1] += 1
        elif not cave_2[pos[1] + 1, pos[0] + 1]:
            pos[0] += 1
            pos[1] += 1
        elif pos == [503 - min_x, 0]:
            out_2 += 1
            stop = True
            break
        else:
            cave_2[pos[1], pos[0]] = True
            out_2 += 1
            break

print(out_2)
