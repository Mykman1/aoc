from aocd import get_data

data = get_data(year=2022, day=4)

inp = [
    [[int(z) for z in y.split("-")] for y in x.split(",")]
    for x in data.split("\n")
]


def check_contained(superset, subset):
    return superset[0] <= subset[0] and superset[1] >= subset[1]


out_1 = 0
for int_1, int_2 in inp:
    if check_contained(int_1, int_2) or check_contained(int_2, int_1):
        out_1 += 1

print(out_1)


def check_overlap(pair_1, pair_2):
    return (pair_1[1] >= pair_2[0]) and (pair_1[0] <= pair_2[1])


out_2 = 0
for int_1, int_2 in inp:
    if check_overlap(int_1, int_2):
        out_2 += 1

print(out_2)
