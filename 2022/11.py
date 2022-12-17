import re
from copy import deepcopy
from math import prod

from aocd import get_data

data = get_data(year=2022, day=11)

inp = [x.split("\n") for x in data.split("\n\n")]

monke_orig = {
    int(re.search(r"(\d+)", lst[0]).group(1)): {
        "items": [
            int(x) for x in lst[1].replace("  Starting items: ", "").split(", ")
        ],
        "operation": lst[2].replace("  Operation: new = ", ""),
        "div_test": int(lst[3].replace("  Test: divisible by ", "")),
        "pass_to": {
            True: int(lst[4].replace("    If true: throw to monkey ", "")),
            False: int(lst[5].replace("    If false: throw to monkey ", "")),
        },
        "times_inspected": 0,
    }
    for lst in inp
}

monke = deepcopy(monke_orig)
for _ in range(20):
    for m, meta in monke.items():
        while meta["items"]:
            meta["times_inspected"] += 1
            old = meta["items"].pop(0)
            new = eval(meta["operation"]) // 3
            monke[meta["pass_to"][new % meta["div_test"] == 0]]["items"].append(
                new
            )

monke_business = sorted(
    [x["times_inspected"] for x in monke.values()], reverse=True
)
out_1 = monke_business[0] * monke_business[1]

print(out_1)

monke = deepcopy(monke_orig)
div_test_prod = prod([x["div_test"] for x in monke.values()])
for i in range(10000):
    for m, meta in monke.items():
        while meta["items"]:
            meta["times_inspected"] += 1
            old = meta["items"].pop(0)
            new = eval(meta["operation"]) % div_test_prod
            monke[meta["pass_to"][new % meta["div_test"] == 0]]["items"].append(
                new
            )

monke_business = sorted(
    [x["times_inspected"] for x in monke.values()], reverse=True
)
out_2 = monke_business[0] * monke_business[1]

print(out_2)
