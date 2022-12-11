import numpy as np
from aocd import get_data

data = get_data(day=15)

inp = np.array([[int(y) for y in x] for x in data.split("\n")])
max_risk = 10 * inp.shape[0] * inp.shape[1]

min_risk = np.full(inp.shape, max_risk)
min_risk[0][0] = inp[0][0]

path_len = np.zeros(inp.shape, dtype=int)
path_len[0][0] = 1

while np.any(min_risk == max_risk):
    risks = np.pad(
        min_risk, ((1, 1), (1, 1)), mode="constant", constant_values=max_risk
    )
    up = np.roll(risks, -1, 0)[1:-1, 1:-1] + inp
    path_len_up = np.roll(path_len, -1, 0)
    down = np.roll(risks, 1, 0)[1:-1, 1:-1] + inp
    path_len_down = np.roll(path_len, 1, 0)
    left = np.roll(risks, -1, 1)[1:-1, 1:-1] + inp
    path_len_left = np.roll(path_len, -1, 1)
    right = np.roll(risks, 1, 1)[1:-1, 1:-1] + inp
    path_len_right = np.roll(path_len, 1, 1)
    ls = [
        (up, path_len_up),
        (down, path_len_down),
        (left, path_len_left),
        (right, path_len_right),
    ]
    mins = [np.min(x[0][path_len == 0]) for x in ls]
    for i in range(len(mins)):
        if mins[i] == min(mins):
            a = ls[i][0]
            b = ls[i][1]
            a[path_len > 0] = max_risk
            x, y = np.unravel_index(np.argmin(a), a.shape)
            min_risk[x, y] = a[x, y]
            path_len[x, y] = b[x, y] + 1
            break
    # print(np.sum(min_risk == max_risk))

min_risk = min_risk - 1

print(min_risk[-1, -1])

inp0 = inp
inp = np.zeros((inp.shape[0] * 5, inp.shape[1] * 5), int)

for i in range(5):
    for j in range(5):
        inp[
            i * inp0.shape[0] : (i + 1) * inp0.shape[0],
            j * inp0.shape[1] : (j + 1) * inp0.shape[1],
        ] = (
            inp0 + i + j
        )

inp -= 1
inp = inp % 9
inp += 1

max_risk = 10 * inp.shape[0] * inp.shape[1]

min_risk = np.full(inp.shape, max_risk)
min_risk[0][0] = inp[0][0]

path_len = np.zeros(inp.shape, dtype=int)
path_len[0][0] = 1

while np.any(min_risk == max_risk):
    risks = np.pad(
        min_risk, ((1, 1), (1, 1)), mode="constant", constant_values=max_risk
    )
    up = np.roll(risks, -1, 0)[1:-1, 1:-1] + inp
    path_len_up = np.roll(path_len, -1, 0)
    down = np.roll(risks, 1, 0)[1:-1, 1:-1] + inp
    path_len_down = np.roll(path_len, 1, 0)
    left = np.roll(risks, -1, 1)[1:-1, 1:-1] + inp
    path_len_left = np.roll(path_len, -1, 1)
    right = np.roll(risks, 1, 1)[1:-1, 1:-1] + inp
    path_len_right = np.roll(path_len, 1, 1)
    ls = [
        (up, path_len_up),
        (down, path_len_down),
        (left, path_len_left),
        (right, path_len_right),
    ]
    mins = [np.min(x[0][path_len == 0]) for x in ls]
    for i in range(len(mins)):
        if mins[i] == min(mins):
            a = ls[i][0]
            b = ls[i][1]
            a[path_len > 0] = max_risk
            x, y = np.unravel_index(np.argmin(a), a.shape)
            min_risk[x, y] = a[x, y]
            path_len[x, y] = b[x, y] + 1
            break
    # print(np.sum(min_risk == max_risk))

min_risk = min_risk - 1

print(min_risk[-1, -1])
