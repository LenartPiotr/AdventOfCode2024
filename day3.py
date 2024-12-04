import re

t = []
with open('./in/d3.txt') as f:
    for l in f:
        t.append(l)
t = ''.join(t)

# part 1
x = re.findall(r'(mul\(\d{1,3},\d{1,3}\))', t)
sum = 0
for mul in x:
    m = re.match(r'mul\((\d+),(\d+)\)', mul)
    sum += int(m.group(1)) * int(m.group(2))
print(sum)

# part 2
start = 0
size = len(t)
sum = 0
while start < size and start != -1:
    end = t.find("don't()", start)
    x = re.findall(r'(mul\(\d{1,3},\d{1,3}\))', t[start:end])
    for mul in x:
        m = re.match(r'mul\((\d+),(\d+)\)', mul)
        sum += int(m.group(1)) * int(m.group(2))
    start = t.find('do()', end)
print(sum)