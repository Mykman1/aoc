from collections import Counter

from aocd import get_data

data = get_data(year=2022, day=9)

inp = [(x[0], int(x[2:])) for x in data.split("\n")]

c = Counter()
c[(0, 0)] += 1
H_pos = 0, 0
HT_diff = 0, 0

dir_map = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

for dir, steps in inp:
    for _ in range(steps):
        H_pos = H_pos[0] + dir_map[dir][0], H_pos[1] + dir_map[dir][1]
        HT_diff = HT_diff[0] + dir_map[dir][0], HT_diff[1] + dir_map[dir][1]
        if HT_diff[0] == 2:
            HT_diff = 1, 0
            c[H_pos[0] - 1, H_pos[1]] += 1
        elif HT_diff[0] == -2:
            HT_diff = -1, 0
            c[H_pos[0] + 1, H_pos[1]] += 1
        elif HT_diff[1] == 2:
            HT_diff = 0, 1
            c[H_pos[0], H_pos[1] - 1] += 1
        elif HT_diff[1] == -2:
            HT_diff = 0, -1
            c[H_pos[0], H_pos[1] + 1] += 1


out_1 = len(c.keys())

print(out_1)

c_2 = Counter()
c_2[(0, 0)] += 1
pos = [(0, 0)] * 10

for dir, steps in inp:
    for _ in range(steps):
        for k in range(10):
            if k == 0:
                pos[k] = (
                    pos[k][0] + dir_map[dir][0],
                    pos[k][1] + dir_map[dir][1],
                )
            else:
                if (
                    abs(pos[k][0] - pos[k - 1][0]) >= 2
                    or abs(pos[k][1] - pos[k - 1][1]) >= 2
                ):
                    if pos[k][0] == pos[k - 1][0] or pos[k][1] == pos[k - 1][1]:
                        potential_dests = [
                            (pos[k][0] + x, pos[k][1] + y)
                            for x, y in dir_map.values()
                        ]
                        dists = {
                            (x, y): abs(x - pos[k - 1][0])
                            + abs(y - pos[k - 1][1])
                            for x, y in potential_dests
                        }
                        min_dist = min(dists.values())
                        pos[k] = [k for k, v in dists.items() if v == min_dist][
                            0
                        ]
                    else:
                        potential_dests = [
                            (pos[k][0] + x, pos[k][1] + y)
                            for x in [-1, 1]
                            for y in [-1, 1]
                        ]
                        dists = {
                            (x, y): abs(x - pos[k - 1][0])
                            + abs(y - pos[k - 1][1])
                            for x, y in potential_dests
                        }
                        min_dist = min(dists.values())
                        pos[k] = [k for k, v in dists.items() if v == min_dist][
                            0
                        ]
        c_2[pos[-1]] += 1

out_2 = len(c_2.keys())

print(out_2)
