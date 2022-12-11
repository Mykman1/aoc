from aocd import get_data

data = get_data(year=2022, day=1)

inp = [[int(y) for y in x.split("\n")] for x in data.split("\n\n")]

out_1 = max([sum(x) for x in inp])

print(out_1)

out_2 = sum(sorted([sum(x) for x in inp])[-3:])

print(out_2)
