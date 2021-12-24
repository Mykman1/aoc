from aocd import get_data

data = get_data(day=24)

inp = [x.split(" ") for x in data.split("\n")]


def parse_b(b, v):
    if b[0] == "-":
        if b[1:].isdigit():
            return int(b)
    elif b.isdigit():
        return int(b)
    else:
        return v[b]


def run_program(x):
    inputs = [int(y) for y in str(x)]
    vars = {"w": 0, "x": 0, "y": 0, "z": 0}
    which_inp = 0
    for cmd in inp:
        instr = cmd[0]
        if instr == "inp":
            vars[cmd[1]] = inputs[which_inp]
            which_inp += 1
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
    if vars["z"] == 0:
        print(vars["z"])
        return x
    return None
