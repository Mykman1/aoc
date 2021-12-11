import numpy as np
from aocd import get_data

data = get_data(day=11)

inp = np.array([[int(x) for x in y] for y in data.split("\n")])

grid = np.pad(inp, 1)

dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

total_flashes = 0

for i in range(100):
    grid[1:-1, 1:-1] += 1
    grid_old = np.zeros(np.shape(grid), dtype=int)
    zeros = (grid == 0) | (grid > 9)
    flashes = np.zeros(np.shape(grid), dtype=bool)
    while np.any(grid != grid_old):
        grid_old = grid.copy()
        nbrs = []
        for d in dirs:
            nbr = np.roll(np.roll(grid, d[0], 0), d[1], 1)
            nbrs.append(1 * (nbr > 9))
        zeros = zeros | (grid == 0) | (grid > 9)
        flashes = flashes | (grid > 9)
        grid += sum(nbrs)
        grid[zeros] = 0
    total_flashes += np.sum(flashes)

print(total_flashes)

grid = np.pad(inp, 1)

dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

n_oct = np.shape(inp)[0] * np.shape(inp)[1]

iter = 0
while True:
    iter += 1
    grid[1:-1, 1:-1] += 1
    grid_old = np.zeros(np.shape(grid), dtype=int)
    zeros = (grid == 0) | (grid > 9)
    flashes = np.zeros(np.shape(grid), dtype=bool)
    while np.any(grid != grid_old):
        grid_old = grid.copy()
        nbrs = []
        for d in dirs:
            nbr = np.roll(np.roll(grid, d[0], 0), d[1], 1)
            nbrs.append(1 * (nbr > 9))
        zeros = zeros | (grid == 0) | (grid > 9)
        flashes = flashes | (grid > 9)
        grid += sum(nbrs)
        grid[zeros] = 0
    if np.sum(flashes) == n_oct:
        break

print(iter)
