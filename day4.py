import re
import numpy as np

t = []
with open('./in/d4.txt') as f:
    for l in f:
        t.append(l)

arr = np.array([list(row.strip()) for row in t])
tv = [''.join(row) for row in arr.T]
size = arr.shape[0]
diagonals = [''.join(arr.diagonal(i)) for i in np.arange(-size, size)]
diagonals2 = [''.join(np.rot90(arr).diagonal(i)) for i in np.arange(-size, size)]

s1 = sum([sum([1 for _ in re.finditer('XMAS', row)]) for row in t])
s2 = sum([sum([1 for _ in re.finditer('SAMX', row)]) for row in t])
s3 = sum([sum([1 for _ in re.finditer('XMAS', row)]) for row in tv])
s4 = sum([sum([1 for _ in re.finditer('SAMX', row)]) for row in tv])
s5 = sum([sum([1 for _ in re.finditer('XMAS', row)]) for row in diagonals])
s6 = sum([sum([1 for _ in re.finditer('SAMX', row)]) for row in diagonals])
s7 = sum([sum([1 for _ in re.finditer('XMAS', row)]) for row in diagonals2])
s8 = sum([sum([1 for _ in re.finditer('SAMX', row)]) for row in diagonals2])

print(s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8)

cords = [(i, j) for i in np.arange(1, size - 1) for j in np.arange(1, size - 1) if arr[i, j] == 'A']
possibilities = [arr[i-1,j-1]+arr[i+1,j-1]+arr[i+1,j+1]+arr[i-1,j+1] for i, j in cords]
print(sum([1 for p in possibilities if p in ['MMSS', 'SMMS', 'SSMM', 'MSSM']]))