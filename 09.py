import numpy as np
from aocd import get_data

data = get_data(day=9)

inp = np.array([[int(y) + 1 for y in x] for x in data.split("\n")])

up = np.pad(inp, ((0, 1), (0, 0)))[1:, :]
down = np.pad(inp, ((1, 0), (0, 0)))[:-1, :]
left = np.pad(inp, ((0, 0), (1, 0)))[:, :-1]
right = np.pad(inp, ((0, 0), (0, 1)))[:, 1:]

up[up == 0] = 10
down[down == 0] = 10
left[left == 0] = 10
right[right == 0] = 10


inp[inp >= up] = 10
inp[inp >= down] = 10
inp[inp >= left] = 10
inp[inp >= right] = 10

print(np.sum(inp[inp != 10]))
