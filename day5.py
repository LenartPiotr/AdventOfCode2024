import numpy as np
from functools import cmp_to_key

t = []
with open('./in/d5.txt') as f:
    for l in f:
        t.append(l.strip())

splitPoint = np.where(np.array(t) == '')[0][0]
rulesText = t[:splitPoint]
pagesText = t[splitPoint+1:]

rules = dict()
for rule in rulesText:
    s = rule.split('|')
    n1, n2 = int(s[0]), int(s[1])
    if n1 in rules:
        rules[n1].append(n2)
    else:
        rules[n1] = [n2]

rulesSet = dict()
for rule in rules:
    rulesSet[rule] = set(rules[rule])

pages = [[int(num) for num in row.split(',')] for row in pagesText]

# Part 1
def correct(page):
    for i in range(len(page)):
        if page[i] in rulesSet:
            if len(set(page[:i]) & rulesSet[page[i]]) > 0:
                return False
    return True

sum = 0
for page in pages:
    if correct(page):
        sum += page[len(page) // 2]
print(sum)

# Part 2
def sortFunc(x1, x2):
    if x1 in rulesSet and x2 in rulesSet[x1]:
        return -1
    if x2 in rulesSet and x1 in rulesSet[x2]:
        return 1
    return 0

sum = 0
for page in pages:
    if not correct(page):
        correctPage = sorted(page, key=cmp_to_key(sortFunc))
        sum += correctPage[len(correctPage) // 2]
print(sum)