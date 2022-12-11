from aocd import get_data

data = get_data(year=2021, day=2)
inp = data.split("\n")

dir_dict = {"up": (0, -1), "down": (0, 1), "forward": (1, 0)}
coords = [
    (dir_dict[y[0]][0] * int(y[1]), dir_dict[y[0]][1] * int(y[1]))
    for y in [x.split(" ") for x in inp]
]
sums = [sum(x) for x in zip(*coords)]

out_1 = sums[0] * sums[1]
print(out_1)

dir_dict_2 = {"up": (0, 0, -1), "down": (0, 0, 1), "forward": (1, 1, 0)}

pos = 0
dep = 0
aim = 0
for y in [x.split(" ") for x in inp]:
    m = int(y[1])
    dir = y[0]
    aim += m * dir_dict_2[dir][2]
    pos += m * dir_dict_2[dir][0]
    dep += m * aim * dir_dict_2[dir][1]

out_2 = pos * dep
print(out_2)
