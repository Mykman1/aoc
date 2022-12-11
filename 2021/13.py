import numpy as np
from aocd import get_data

data = get_data(year=2021, day=13)

inp, folds = data.split("\n\n")
inp = [tuple(int(y) for y in x.split(",")) for x in inp.split("\n")]
folds = [(x.split("=")[0][-1], int(x.split("=")[1])) for x in folds.split("\n")]

dim_x = max([x[1] for x in folds if x[0] == "x"]) * 2 + 1
dim_y = max([x[1] for x in folds if x[0] == "y"]) * 2 + 1

paper = np.zeros((dim_y, dim_x), dtype=bool)

for i, j in inp:
    paper[j, i] = True

flip_axis = {"x": 1, "y": 0}

for r in range(1):
    paper = paper | np.flip(paper, axis=flip_axis[folds[r][0]])
    if folds[r][0] == "x":
        paper = paper[:, : folds[r][1]]
    else:
        paper = paper[: folds[r][1], :]

print(np.sum(paper))

paper = np.zeros((dim_y, dim_x), dtype=bool)

for i, j in inp:
    paper[j, i] = True

flip_axis = {"x": 1, "y": 0}

for r in range(len(folds)):
    paper = paper | np.flip(paper, axis=flip_axis[folds[r][0]])
    if folds[r][0] == "x":
        paper = paper[:, : folds[r][1]]
    else:
        paper = paper[: folds[r][1], :]

chars = {True: "##", False: "  "}


for row in paper:
    print("".join([chars[x] for x in row]))
