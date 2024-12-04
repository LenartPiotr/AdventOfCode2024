import numpy as np

t = []
with open('./in/d2.txt') as f:
    for l in f:
        l = [int(s) for s in l.strip().split()]
        t.append(l)

def isSafe(row):
    s = set(row[1:] - row[:-1])
    return len(s - {1, 2, 3}) == 0 or len(s - {-1, -2, -3}) == 0

part1 = 0
part2 = 0
for r in t:
    r = np.array(r)
    if isSafe(r):
        part1 += 1
    else:
        for i in range(len(r)):
            if isSafe(np.delete(r, i)):
                part2 += 1
                break
print(part1)
print(part1 + part2)