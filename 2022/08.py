import numpy as np
from aocd import get_data

data = get_data(year=2022, day=8)

inp = np.array([[c for c in col] for col in data.split("\n")], dtype=int)

out_1 = 2 * inp.shape[0] + 2 * inp.shape[1] - 4
for i in range(1, inp.shape[0] - 1):
    for j in range(1, inp.shape[1] - 1):
        if (
            min(
                np.max(inp[:i, j]),
                np.max(inp[i + 1 :, j]),
                np.max(inp[i, :j]),
                np.max(inp[i, j + 1 :]),
            )
            < inp[i, j]
        ):
            out_1 += 1

print(out_1)

inp_2 = inp.copy()
inp_2[[0, -1], :] = 10
inp_2[:, [0, -1]] = 10

out_2 = 0
for i in range(1, inp_2.shape[0] - 1):
    for j in range(1, inp_2.shape[1] - 1):
        h = inp_2[i, j]
        score_up = i - np.max(np.argwhere(inp_2[:i, j] >= h))
        score_down = np.min(np.argwhere(inp_2[i + 1 :, j] >= h)) + 1
        score_left = j - np.max(np.argwhere(inp_2[i, :j] >= h))
        score_right = np.min(np.argwhere(inp_2[i, j + 1 :] >= h)) + 1
        out_2 = max(out_2, score_up * score_down * score_left * score_right)

print(out_2)
