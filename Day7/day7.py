
cwd = [] #stack to keep track of current location NEEDS TO BE FULL PATH
size = {} #dictionary of current directory size
subdirs = {} #unused, part of an earlier idea

with open('input.txt', 'r') as f:
  for line in f:
    line = line.rstrip().split()
    if(line[0] == '$'):
      if(line[1] == 'ls'): pass
      elif(line[2] == '..'):
        size[cwd[-2]] += size[cwd[-1]]
        cwd.pop()
      else:
        cwd.append("".join(cwd)+line[2])
        size[cwd[-1]] = 0
        subdirs[cwd[-1]] = []
    elif(line[0] == 'dir'):
      subdirs[cwd[-1]].append(line[1])
    else: size[cwd[-1]] += int(line[0])

for x in range(len(cwd)-1):
  size[cwd[-2]] += size[cwd[-1]]
  cwd.pop()
  
print(sum([x for x in list(size.values()) if x <= 100000]))
