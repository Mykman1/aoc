from aocd import get_data

data = get_data(year=2022, day=2)

inp = [tuple(x.split(" ")) for x in data.split("\n")]

scores_1 = {
    "A": {"X": 1 + 3, "Y": 2 + 6, "Z": 3 + 0},
    "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
    "C": {"X": 1 + 6, "Y": 2 + 0, "Z": 3 + 3},
}

out_1 = 0
for x, y in inp:
    out_1 += scores_1[x][y]

out_1 = max([sum(x) for x in inp])

print(out_1)

scores_2 = {
    "A": {"X": 3 + 0, "Y": 1 + 3, "Z": 2 + 6},
    "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
    "C": {"X": 2 + 0, "Y": 3 + 3, "Z": 1 + 6},
}

out_2 = 0
for x, y in inp:
    out_2 += scores_2[x][y]

print(out_2)
