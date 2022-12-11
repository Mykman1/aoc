import re
from copy import deepcopy

from aocd import get_data

data = get_data(year=2022, day=5)

inp = [[y + " " for y in x.split("\n")] for x in data.split("\n\n")]
n_stacks = len(inp[0][0]) // 4
stacks_orig = {x + 1: [] for x in range(n_stacks)}
for row in reversed(inp[0][:-1]):
    for stack in range(n_stacks):
        x = row[4 * stack + 1]
        if x != " ":
            stacks_orig[stack + 1].append(x)

moves = [
    [
        int(x)
        for x in re.search(r"^move (\d+) from (\d+) to (\d+) $", x).groups()
    ]
    for x in inp[1]
]

stacks = deepcopy(stacks_orig)

for m, f, t in moves:
    for n in range(m):
        stacks[t].append(stacks[f].pop())

out_1 = "".join([x[-1] for x in stacks.values()])

print(out_1)

stacks = deepcopy(stacks_orig)

for m, f, t in moves:
    buff = []
    for n in range(m):
        buff.append(stacks[f].pop())
    stacks[t] = stacks[t] + list(reversed(buff))

out_2 = "".join([x[-1] for x in stacks.values()])

print(out_2)
