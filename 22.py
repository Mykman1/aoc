import re
from collections import Counter

import numpy as np
from aocd import get_data

data = get_data(day=22)

inp = [
    re.search(
        r"^(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$",
        x,
    )
    for x in data.split("\n")
]
inp = [
    (
        x.group(1),
        int(x.group(2)),
        int(x.group(3)),
        int(x.group(4)),
        int(x.group(5)),
        int(x.group(6)),
        int(x.group(7)),
    )
    for x in inp
]

x = np.zeros((101, 101, 101), dtype=bool)
for t in inp:
    x[
        max(0, t[1] + 50) : min(101, t[2] + 51),
        max(0, t[3] + 50) : min(101, t[4] + 51),
        max(0, t[5] + 50) : min(101, t[6] + 51),
    ] = (
        t[0] == "on"
    )

print(np.sum(x))


def vol(x1, x2, y1, y2, z1, z2):
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


def intersect(t1, t2):
    if (
        t1[0] <= t2[1]
        and t2[0] <= t1[1]
        and t1[2] <= t2[3]
        and t2[2] <= t1[3]
        and t1[4] <= t2[5]
        and t2[4] <= t1[5]
    ):
        return (
            max(t1[0], t2[0]),
            min(t1[1], t2[1]),
            max(t1[2], t2[2]),
            min(t1[3], t2[3]),
            max(t1[4], t2[4]),
            min(t1[5], t2[5]),
        )
    return None


current_blocks = Counter()
for u in range(len(inp)):
    t = inp[u]
    current_blocks_new = Counter()
    for j in current_blocks.keys():
        i = intersect(j, t[1:])
        if i:
            current_blocks_new[i] -= current_blocks[j]
    current_blocks.update(current_blocks_new)
    if t[0] == "on":
        current_blocks[tuple(t[1:])] += 1
    for k in list(current_blocks.keys()):
        if current_blocks[k] == 0:
            del current_blocks[k]

print(sum([current_blocks[x] * vol(*x) for x in current_blocks.keys()]))
