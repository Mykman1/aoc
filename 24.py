from aocd import get_data

data = get_data(day=24)

inp = [x.split(" ") for x in data.split("\n")]

inp_split = [
    [y.split(" ") for y in ("i" + x).split("\n")] for x in data[1:].split("\ni")
]


def parse_b(b, v):
    if b in ["w", "x", "y", "z"]:
        return v[b]
    else:
        return int(b)


def run_command(transforms, inp, z):
    vars = {"w": 0, "x": 0, "y": 0, "z": z}
    for cmd in transforms:
        instr = cmd[0]
        if instr == "inp":
            vars[cmd[1]] = inp
        elif instr == "add":
            vars[cmd[1]] += parse_b(cmd[2], vars)
        elif instr == "mul":
            vars[cmd[1]] *= parse_b(cmd[2], vars)
        elif instr == "div":
            vars[cmd[1]] //= parse_b(cmd[2], vars)
        elif instr == "mod":
            vars[cmd[1]] %= parse_b(cmd[2], vars)
        elif instr == "eql":
            vars[cmd[1]] = int(vars[cmd[1]] == parse_b(cmd[2], vars))
        else:
            raise Exception
    return vars


rules = [(int(x[4][2]), int(x[5][2]), int(x[-3][2])) for x in inp_split]
nines = 9699999  # Chepaev's constant
nine_c = 0
while True:
    ds = []
    zs = []
    z = 0
    nn = [int(y) for y in str(nines - nine_c)]
    which_nine = 0
    for i in range(len(inp_split)):
        if rules[i][0] == 1:
            d = nn[which_nine]
            which_nine += 1
        else:
            d = z % 26 + rules[i][1]
        z = run_command(inp_split[i], d, z)["z"]
        zs.append(z)
        ds.append(d)
    nine_c += 1
    if len([x for x in ds if 1 <= x <= 9]) == len(inp_split):
        break

print("".join([str(x) for x in ds]))


rules = [(int(x[4][2]), int(x[5][2]), int(x[-3][2])) for x in inp_split]
ones = 5131111  # Chepaev's constant
one_c = 0
while True:
    ds = []
    zs = []
    z = 0
    nn = [int(y) for y in str(ones + one_c)]
    which_one = 0
    for i in range(len(inp_split)):
        if rules[i][0] == 1:
            d = nn[which_one]
            which_one += 1
        else:
            d = z % 26 + rules[i][1]
        z = run_command(inp_split[i], d, z)["z"]
        zs.append(z)
        ds.append(d)
    one_c += 1
    if len([x for x in ds if 1 <= x <= 9]) == len(inp_split):
        break

print("".join([str(x) for x in ds]))
