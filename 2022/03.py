from aocd import get_data

data = get_data(year=2022, day=3)

inp = data.split("\n")
inp_1 = [tuple([x[: (len(x) // 2)], x[(len(x) // 2) :]]) for x in inp]


def get_priority(item):
    return ord(item) - 96 if item >= "a" else ord(item) - 38


out_1 = sum([get_priority(list(set(x).intersection(y))[0]) for x, y in inp_1])

print(out_1)

inp_2 = []
for i in range(len(inp) // 3):
    inp_2.append(tuple([inp[3 * i], inp[3 * i + 1], inp[3 * i + 2]]))

out_2 = sum(
    [
        get_priority(list(set(x).intersection(y).intersection(z))[0])
        for x, y, z in inp_2
    ]
)

print(out_2)
