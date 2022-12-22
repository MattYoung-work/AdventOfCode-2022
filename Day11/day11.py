i = 0
items = {}
op = {}
test = {}
dt = {}
df = {}
count = []
worry = 1

with open('./input.txt','r') as f:
  for line in f:
    foo = line.strip().split()
    if not foo: pass
    elif foo[0] == 'Monkey': i = int(foo[1][:-1])
    elif foo[0] == 'Starting': items[i] = [int(x.strip(',')) for x in foo[2:]]
    elif foo[0] == 'Operation:':  op[i] = ''.join(foo[1:])
    elif foo[0] == 'Test:': test[i] = int(foo[-1])
    elif foo[0] == 'If':
      if foo[1] == 'true:': dt[i] = int(foo[-1])
      elif foo[1] == 'false:': df[i] = int(foo[-1])

for i in range(len(items)): count.append(0)
for i in range(len(items)): worry *= test[i]

for n in range(20):
  for i in range(len(items)):
    for old in items[i]:
      count[i] += 1
      exec(op[i])
      new = new // 3
      if new % test[i] == 0: items[dt[i]].append(new)
      else: items[df[i]].append(new)
    items[i] = []

for i in range(len(items)):
  print(f'Monkey {i} inspected {count[i]} items')

count.sort()
print(count[-1] * count[-2])
