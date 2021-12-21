import re
from collections import Counter

from aocd import get_data

data = get_data(day=21)

inp = [int(re.search(r"\d+$", x).group(0)) for x in data.split("\n")]

rolls = 0
cur_pos = inp
pts = [0, 0]
whose_turn = 0

while max(pts) < 1000:
    rolls += 3
    cur_pos[whose_turn] = (
        (cur_pos[whose_turn] + 3 * ((rolls - 1) % 100 + 1) - 4) % 10
    ) + 1
    pts[whose_turn] += cur_pos[whose_turn]
    whose_turn = 1 - whose_turn

print(pts[whose_turn] * rolls)

inp = [int(re.search(r"\d+$", x).group(0)) for x in data.split("\n")]

pts = [0, 0]
rolls = 0
universes = [Counter()]
universes[0][tuple(inp + pts)] = 1
while True:
    new_universes = Counter()
    if len(universes[rolls].keys()) == 0:
        break
    for k in list(universes[rolls].keys()):
        cur_pos = list(k[:2])
        pts = list(k[2:])
        if max(pts) >= 21:
            continue
        whose_turn = rolls % 2
        cur_pos[whose_turn] = [
            (cur_pos[whose_turn] + x + y + z - 1) % 10 + 1
            for x in [1, 2, 3]
            for y in [1, 2, 3]
            for z in [1, 2, 3]
        ]
        cur_pos[1 - whose_turn] = [cur_pos[1 - whose_turn]]
        pts[whose_turn] = [pts[whose_turn] + x for x in cur_pos[whose_turn]]
        pts[1 - whose_turn] = [pts[1 - whose_turn]]
        for i in range(len(cur_pos[0])):
            for j in range(len(cur_pos[1])):
                new_universes[
                    (cur_pos[0][i], cur_pos[1][j], pts[0][i], pts[1][j])
                ] += universes[rolls][k]
    universes.append(new_universes)
    rolls += 1

print(
    max(
        sum([x[y] for x in universes for y in x.keys() if y[2] >= 21]),
        sum([x[y] for x in universes for y in x.keys() if y[3] >= 21]),
    )
)
