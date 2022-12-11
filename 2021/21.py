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
cts = Counter(
    [x + y + z for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3]]
)
while True:
    new_universes = Counter()
    if len(universes[rolls].keys()) == 0:
        break
    for k in list(universes[rolls].keys()):
        cur_pos = list(k[:2])
        pts = list(k[2:])
        if max(pts) >= 21:
            continue
        if rolls % 2:
            for pt, t in cts.items():
                new_universes[
                    (
                        cur_pos[0],
                        (cur_pos[1] + pt - 1) % 10 + 1,
                        pts[0],
                        pts[1] + (cur_pos[1] + pt - 1) % 10 + 1,
                    )
                ] += (
                    universes[rolls][k] * t
                )
        else:
            for pt, t in cts.items():
                new_universes[
                    (
                        (cur_pos[0] + pt - 1) % 10 + 1,
                        cur_pos[1],
                        pts[0] + (cur_pos[0] + pt - 1) % 10 + 1,
                        pts[1],
                    )
                ] += (
                    universes[rolls][k] * t
                )
    universes.append(new_universes)
    rolls += 1

print(
    max(
        sum([x[y] for x in universes for y in x.keys() if y[2] >= 21]),
        sum([x[y] for x in universes for y in x.keys() if y[3] >= 21]),
    )
)
