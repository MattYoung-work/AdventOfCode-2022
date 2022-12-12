x = 1
X = {1:1}
cnt = 1

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
print(20 * X[20] + 60 * X[60] + 100 * X[100] + 140 * X[140] + 180 * X[180] + 220 * X[220])