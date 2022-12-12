x = 1
X = {1:1}
cnt = 1
crt = [['.' for x in range(40)] for x in range(6)]
with open('input.txt', 'r') as f:
  for line in f:
    line = line.rstrip().split()
    if (line[0] == 'noop'):
      cnt += 1
      X[cnt] = x
    elif (line[0] == 'addx'):
      cnt += 1
      X[cnt] = x
      cnt += 1
      x = x + int(line[1])
      X[cnt] = x
    else: pass

for i in range(240):
  a = int(i / 40)
  b = i % 40
  pos = X[i+1]
  if (abs(pos - b) < 2): crt[a][b] = '#'

for i in range(6):
  print(''.join(crt[i]))