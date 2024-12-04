import numpy as np

t = []
with open('./in/d1.txt') as f:
    for l in f:
        l = [int(s) for s in l.strip().split()]
        t.append(l)
t = np.array(t)

# part 1
t1 = t.copy()
t1[:,0] = np.sort(t1[:,0])
t1[:,1] = np.sort(t1[:,1])
print(np.sum(np.abs(t1[:,0] - t1[:,1])))

# part 2
s = 0
for i in t[:,0]:
    s += i * np.sum(t[:,1] == i)
print(s)
