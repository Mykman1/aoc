from math import prod

import numpy as np
from aocd import get_data

data = get_data(day=9)

inp = np.array([[int(y) + 1 for y in x] for x in data.split("\n")])

up = np.pad(inp, ((0, 1), (0, 0)))[1:, :]
down = np.pad(inp, ((1, 0), (0, 0)))[:-1, :]
left = np.pad(inp, ((0, 0), (0, 1)))[:, 1:]
right = np.pad(inp, ((0, 0), (1, 0)))[:, :-1]

up[up == 0] = 10
down[down == 0] = 10
left[left == 0] = 10
right[right == 0] = 10


inp[inp >= up] = 10
inp[inp >= down] = 10
inp[inp >= left] = 10
inp[inp >= right] = 10

print(np.sum(inp[inp != 10]))

inp = np.array([[int(y) + 1 for y in x] for x in data.split("\n")])

up = np.pad(inp, ((0, 1), (0, 0)))[1:, :]
down = np.pad(inp, ((1, 0), (0, 0)))[:-1, :]
left = np.pad(inp, ((0, 0), (0, 1)))[:, 1:]
right = np.pad(inp, ((0, 0), (1, 0)))[:, :-1]

up[up == 0] = 10
down[down == 0] = 10
left[left == 0] = 10
right[right == 0] = 10

flow = 1 * (inp != 10)
flow_prev = np.zeros(np.shape(inp), dtype=int)

while np.any(flow_prev != flow):
    flow_prev = flow.copy()
    for i in range(np.shape(inp)[0]):
        for j in range(np.shape(inp)[1]):
            if up[i, j] != 10 and flow[i + 1, j] > 0 and inp[i, j] < up[i, j]:
                flow[i, j] += flow[i + 1, j]
                flow[i + 1, j] = 0
            if (
                down[i, j] != 10
                and flow[i - 1, j] > 0
                and inp[i, j] < down[i, j]
            ):
                flow[i, j] += flow[i - 1, j]
                flow[i - 1, j] = 0
            if (
                left[i, j] != 10
                and flow[i, j + 1] > 0
                and inp[i, j] < left[i, j]
            ):
                flow[i, j] += flow[i, j + 1]
                flow[i, j + 1] = 0
            if (
                right[i, j] != 10
                and flow[i, j - 1] > 0
                and inp[i, j] < right[i, j]
            ):
                flow[i, j] += flow[i, j - 1]
                flow[i, j - 1] = 0

print(prod(sorted(flow[flow > 0])[-3:]))
