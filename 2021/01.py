from aocd import get_data

data = get_data(year=2021, day=1)

inp = [int(x) for x in data.split("\n")]

comp = zip(inp[1:], inp[:-1])
out_1 = len([x for x in comp if x[0] > x[1]])

print(out_1)

comp = zip(inp[3:], inp[:-3])
out_2 = len([x for x in comp if x[0] > x[1]])

print(out_2)
