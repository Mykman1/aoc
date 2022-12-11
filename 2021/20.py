import numpy as np
from aocd import get_data

data = get_data(day=20)

inp = data.split("\n\n")
algo = [
    int(x) for x in inp[0].replace("\n", "").replace("#", "1").replace(".", "0")
]
init = np.array(
    [
        [int(y) for y in x]
        for x in inp[1].replace("#", "1").replace(".", "0").split("\n")
    ]
)
mask = np.array([2 ** x for x in range(8, -1, -1)]).reshape((3, 3))

first_last = [algo[0], algo[-1]]
cur_bounds = 0
cur = np.pad(init, 2, mode="constant", constant_values=cur_bounds)

for i in range(50):
    view_shape = tuple(np.subtract(cur.shape, mask.shape) + 1) + mask.shape
    strides = cur.strides + cur.strides
    sub_matrices = np.lib.stride_tricks.as_strided(cur, view_shape, strides)
    cur = np.einsum("kl,ijkl->ij", mask, sub_matrices)
    for j in range(len(cur)):
        for k in range(len(cur[j])):
            cur[j, k] = algo[cur[j, k]]
    cur_bounds = first_last[cur_bounds]
    cur = np.pad(cur, 2, mode="constant", constant_values=cur_bounds)
    if i == 1:
        print(np.sum(cur))

print(np.sum(cur))
