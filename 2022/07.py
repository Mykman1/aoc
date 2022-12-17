import re
from copy import deepcopy

from aocd import get_data

data = get_data(year=2022, day=7)

inp_orig = [x.split("\n") for x in ("\n" + data).split("\n$ ")[1:]]

fs = {"/root/": 0}
current_path = "/root/"

inp = deepcopy(inp_orig)
for term_line in inp:
    cmd = term_line.pop(0)
    if cmd == "cd /":
        current_path = "/root/"
        continue
    elif cmd == "ls":
        for cmd_output in term_line:
            size, file = cmd_output.split(" ")
            if size == "dir":
                fs[current_path + file + "/"] = 0
            else:
                fs[current_path + file] = int(size)
    elif cmd.startswith("cd "):
        dest = cmd[3:]
        if dest == "..":
            current_path = re.search("^(.*/)[^/]+/$", current_path).group(1)
        else:
            current_path = current_path + dest + "/"


def get_size(path):
    if fs[path] > 0:
        return fs[path]
    else:
        return sum(
            [
                get_size(subpath)
                for subpath in fs.keys()
                if re.match("^" + path + "[^/]+/?$", subpath)
            ]
        )


dir_sizes = {x: get_size(x) for x in fs.keys() if x.endswith("/")}

out_1 = sum([y for _, y in dir_sizes.items() if y <= 100000])

print(out_1)

out_2 = min(
    [y for _, y in dir_sizes.items() if y >= dir_sizes["/root/"] - 40000000]
)

print(out_2)
