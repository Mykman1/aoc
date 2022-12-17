import numpy as np
from aocd import get_data

data = get_data(year=2022, day=12)

inp = np.array([[ord(y) - ord("a") for y in x] for x in data.split("\n")])
inp = np.pad(inp, 1, constant_values=99)
S_pos = list(
    zip(
        np.where(inp == ord("S") - ord("a"))[0],
        np.where(inp == ord("S") - ord("a"))[1],
    )
)[0]
E_pos = list(
    zip(
        np.where(inp == ord("E") - ord("a"))[0],
        np.where(inp == ord("E") - ord("a"))[1],
    )
)[0]
inp[S_pos] = 0
inp[E_pos] = ord("z") - ord("a")
inf = float("inf")

dist_map = {}
nbr_map = {}
for i in range(1, inp.shape[0] - 1):
    for j in range(1, inp.shape[1] - 1):
        get_from = []
        if inp[i + 1, j] - inp[i, j] >= -1 and inp[i + 1, j] != 99:
            get_from.append((i + 1, j))
        if inp[i - 1, j] - inp[i, j] >= -1 and inp[i - 1, j] != 99:
            get_from.append((i - 1, j))
        if inp[i, j + 1] - inp[i, j] >= -1 and inp[i, j + 1] != 99:
            get_from.append((i, j + 1))
        if inp[i, j - 1] - inp[i, j] >= -1 and inp[i, j - 1] != 99:
            get_from.append((i, j - 1))
        nbr_map[(i, j)] = get_from
        dist_map[(i, j)] = inf

dist_map[S_pos] = 0
while dist_map[E_pos] == inf:
    min_dists = {
        k: min([dist_map[x] for x in v] + [inf])
        for k, v in nbr_map.items()
        if dist_map[k] == inf
    }
    min_available_dist = min([x for x in min_dists.values()])
    for node in [k for k, v in min_dists.items() if v == min_available_dist]:
        dist_map[node] = min_available_dist + 1

out_1 = dist_map[E_pos]

print(out_1)

dist_map = {}
nbr_map = {}
for i in range(1, inp.shape[0] - 1):
    for j in range(1, inp.shape[1] - 1):
        get_from = []
        if inp[i + 1, j] - inp[i, j] <= 1 and inp[i + 1, j] != 99:
            get_from.append((i + 1, j))
        if inp[i - 1, j] - inp[i, j] <= 1 and inp[i - 1, j] != 99:
            get_from.append((i - 1, j))
        if inp[i, j + 1] - inp[i, j] <= 1 and inp[i, j + 1] != 99:
            get_from.append((i, j + 1))
        if inp[i, j - 1] - inp[i, j] <= 1 and inp[i, j - 1] != 99:
            get_from.append((i, j - 1))
        nbr_map[(i, j)] = get_from
        dist_map[(i, j)] = inf

dist_map[E_pos] = 0
out_2 = 0
while out_2 == 0:
    min_dists = {
        k: min([dist_map[x] for x in v] + [inf])
        for k, v in nbr_map.items()
        if dist_map[k] == inf
    }
    min_available_dist = min([x for x in min_dists.values()])
    for node in [k for k, v in min_dists.items() if v == min_available_dist]:
        dist_map[node] = min_available_dist + 1
        if inp[node] == 0:
            out_2 = dist_map[node]

print(out_2)
