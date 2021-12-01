with open("input/01", "r") as f:
    in_1 = f.read().split("\n")
    in_1 = [int(x) for x in in_1]

comp = zip(in_1[1:], in_1[:-1])
out_1 = len([x for x in comp if x[0] > x[1]])

print(out_1)

in_2 = in_1

sums = [x[0] + x[1] + x[2] for x in zip(in_2[2:], in_2[1:-1], in_2[:-2])]
comp = zip(sums[1:], sums[:-1])
out_2 = len([x for x in comp if x[0] > x[1]])

print(out_2)
