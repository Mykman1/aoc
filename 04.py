from aocd import get_data
import numpy as np

data = get_data(day=4)
in_1 = data.split("\n\n")

nums = [int(x) for x in in_1[0].split(',')]
bingos_int = [[int(y) for y in x.strip().replace('\n', ' ').replace('  ', ' ').split(' ')] for x in in_1[1:]]
games = len(bingos_int)

bingos = np.reshape(bingos_int, (games, 5, 5))

try:
    for n in nums:
        bingos[bingos == n] = -1
        for g in range(games):
            for i in range(5):
                if all(bingos[g,i,:] == -1) or all(bingos[g,:,i] == -1):
                    unmarked = sum(bingos[g][bingos[g] != -1])
                    print(unmarked * n)
                    raise StopIteration
except StopIteration: pass

in_2 = in_1

nums = [int(x) for x in in_1[0].split(',')]
bingos_int = [[int(y) for y in x.strip().replace('\n', ' ').replace('  ', ' ').split(' ')] for x in in_1[1:]]
games = len(bingos_int)

bingos = np.reshape(bingos_int, (games, 5, 5))

losers = {x for x in range(games)}

for n in nums:
    bingos[bingos == n] = -1
    losers_iter = losers.copy()
    for g in losers_iter:
        for i in range(5):
            if all(bingos[g,i,:] == -1) or all(bingos[g,:,i] == -1):
                losers.remove(g)
                last_winner = g
                break
    if len(losers) == 0:
        unmarked = sum(bingos[last_winner][bingos[last_winner] != -1])
        print(unmarked * n)
        break

