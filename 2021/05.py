import numpy as np
from aocd import get_data

data = get_data(year=2021, day=5)
inp = data.split("\n")

proc = [
    [tuple([int(z) for z in y.split(",")]) for y in x.split(" -> ")]
    for x in inp
]

lines = np.zeros((len(proc), 1000, 1000), dtype=int)

for i in range(len(proc)):
    ax = proc[i][0][0]
    ay = proc[i][0][1]
    bx = proc[i][1][0]
    by = proc[i][1][1]
    ln = max(abs(bx - ax), abs(by - ay)) + 1
    dir_x = np.sign(bx - ax)
    dir_y = np.sign(by - ay)
    if dir_x != 0 and dir_y != 0:
        continue
    for s in range(ln):
        lines[i, ax + s * dir_x, ay + s * dir_y] = 1

print(sum(sum(sum(lines) >= 2)))

proc = [
    [tuple([int(z) for z in y.split(",")]) for y in x.split(" -> ")]
    for x in inp
]

lines = np.zeros((len(proc), 1000, 1000), dtype=int)

for i in range(len(proc)):
    ax = proc[i][0][0]
    ay = proc[i][0][1]
    bx = proc[i][1][0]
    by = proc[i][1][1]
    ln = max(abs(bx - ax), abs(by - ay)) + 1
    dir_x = np.sign(bx - ax)
    dir_y = np.sign(by - ay)
    for s in range(ln):
        lines[i, ax + s * dir_x, ay + s * dir_y] = 1

print(np.sum(sum(lines) >= 2))
