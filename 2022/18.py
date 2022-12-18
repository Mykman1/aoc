import numpy as np
from aocd import get_data

data = get_data(year=2022, day=18)

inp = np.array([[int(y) for y in x.split(",")] for x in data.split("\n")])
mins = inp.min(axis=0)
maxs = inp.max(axis=0)

cubes = np.zeros(shape=maxs - mins + 3, dtype=bool)
for i, j, k in inp:
    cubes[i - mins[0] + 1, j - mins[1] + 1, k - mins[2] + 1] = True

out_1 = (
    6 * np.sum(cubes)
    - 2 * np.sum(cubes[1:, :, :] & cubes[:-1, :, :])
    - 2 * np.sum(cubes[:, 1:, :] & cubes[:, :-1, :])
    - 2 * np.sum(cubes[:, :, 1:] & cubes[:, :, :-1])
)

print(out_1)

inf = float("inf")
nbr_map = {}
lava = np.pad(cubes, 1, constant_values=False)
for i in range(1, lava.shape[0] - 1):
    for j in range(1, lava.shape[1] - 1):
        for k in range(1, lava.shape[2] - 1):
            if not lava[i, j, k]:
                get_from = []
                if not lava[i + 1, j, k] and i < cubes.shape[0]:
                    get_from.append((i, j - 1, k - 1))
                if not lava[i - 1, j, k] and i > 1:
                    get_from.append((i - 2, j - 1, k - 1))
                if not lava[i, j + 1, k] and j < cubes.shape[1]:
                    get_from.append((i - 1, j, k - 1))
                if not lava[i, j - 1, k] and j > 1:
                    get_from.append((i - 1, j - 2, k - 1))
                if not lava[i, j, k + 1] and k < cubes.shape[2]:
                    get_from.append((i - 1, j - 1, k))
                if not lava[i, j, k - 1] and k > 1:
                    get_from.append((i - 1, j - 1, k - 2))
                nbr_map[(i - 1, j - 1, k - 1)] = get_from

dist_map = {
    (x, y, z): inf
    for x in range(cubes.shape[0])
    for y in range(cubes.shape[1])
    for z in range(cubes.shape[2])
}
for i, j, k in inp:
    dist_map.pop((i - mins[0] + 1, j - mins[1] + 1, k - mins[2] + 1))

dist_map[(0, 0, 0)] = 0

last_min_available_dist = 0
min_available_dist = -1
while min_available_dist != last_min_available_dist:
    last_min_available_dist = min_available_dist
    min_dists = {
        k: min([dist_map[x] for x in v] + [inf])
        for k, v in nbr_map.items()
        if dist_map[k] == inf
    }
    min_available_dist = min([x for x in min_dists.values()])
    for node in [k for k, v in min_dists.items() if v == min_available_dist]:
        dist_map[node] = min_available_dist + 1

cubes_with_interior = cubes.copy()
for interior_cube in [k for k, v in min_dists.items() if v == inf]:
    cubes_with_interior[interior_cube] = True

out_2 = (
    6 * np.sum(cubes_with_interior)
    - 2 * np.sum(cubes_with_interior[1:, :, :] & cubes_with_interior[:-1, :, :])
    - 2 * np.sum(cubes_with_interior[:, 1:, :] & cubes_with_interior[:, :-1, :])
    - 2 * np.sum(cubes_with_interior[:, :, 1:] & cubes_with_interior[:, :, :-1])
)

print(out_2)
