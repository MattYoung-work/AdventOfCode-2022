hx = 0
hy = 0
tx = 0
ty = 0

t_coords = {'00':1}

with open('./input.txt','r') as f:
  for line in f:
    line = line.rstrip().split()
    dir = line[0]
    cnt = int(line[1])
    for i in range(cnt):
      #move head
      if (dir == 'R'): hx += 1
      elif (dir == 'U'): hy += 1
      elif (dir == 'L'): hx -= 1
      elif (dir == 'D'): hy -= 1
      else: pass
      #move tail
      if (hx == tx):
        a = hy - ty
        if (a == 1): pass
        elif (a == -1): pass
        elif (a == 2): ty += 1
        elif (a == -2): ty -= 1
        else: pass
      elif (hy == ty):
        a = hx - tx
        if (a == 1): pass
        elif (a == -1): pass
        elif (a ==2): tx += 1
        elif (a == -2): tx -= 1
        else: pass
      else:
        a = hx - tx
        b = hy - ty
        if (abs(a) == 1 and abs(b) == 1): pass
        elif (a == 2):
          ty = hy
          tx = hx -1
        elif (a == -2):
          ty = hy
          tx = hx + 1
        elif (b == 2):
          tx = hx
          ty = hy -1
        elif ( b == -2):
          tx = hx
          ty = hy + 1
        else: pass
      t_coords[str(tx)+str(ty)]=1

print(len(list(t_coords)))