from aocd import get_data

data = get_data(day=1)

in_1 = [int(x) for x in data.split("\n")]

comp = zip(in_1[1:], in_1[:-1])
out_1 = len([x for x in comp if x[0] > x[1]])

print(out_1)

in_2 = in_1

comp = zip(in_2[3:], in_2[:-3])
out_2 = len([x for x in comp if x[0] > x[1]])

print(out_2)
