from aocd import get_data

data = get_data(day=10)

inp = data.split("\n")

pts = {")": 3, "]": 57, "}": 1197, ">": 25137}
pts2 = {"(": 1, "[": 2, "{": 3, "<": 4}

score = 0
score2 = []

for y in inp:
    x = y
    x_old = ""
    while True:
        x = (
            x.replace("()", "")
            .replace("[]", "")
            .replace("{}", "")
            .replace("<>", "")
        )
        if x == x_old:
            break
        x_old = x
    bad = [x.find(b) for b in ")]}>" if x.find(b) > -1]
    if bad:
        score += pts[x[min(bad)]]
    else:
        temp_score2 = 0
        for i in range(len(x) - 1, -1, -1):
            temp_score2 = 5 * temp_score2 + pts2[x[i]]
        score2.append(temp_score2)

print(score)
print(sorted(score2)[(len(score2) - 1) // 2])
