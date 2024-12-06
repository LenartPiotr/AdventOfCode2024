import numpy as np

t = []
with open('./in/d6.txt') as f:
    for l in f:
        t.append(list(l.strip()))
t = np.array(t)

start = np.array(np.where(t == '^'))[:, 0]
direction = np.array([-1, 0])

def inArea(point):
    return 0 <= point[0] < t.shape[0] and 0 <= point[1] <= t.shape[1]

a = t.copy()
pos = start.copy()
dir = direction.copy()
while inArea(pos):
    a[pos[0], pos[1]] = 'X'
    next = pos + dir
    if not inArea(next):
        break
    if a[next[0], next[1]] == '#':
        dir[0], dir[1] = dir[1], -dir[0]
        next = pos
    pos = next

print(np.sum(a == 'X'))