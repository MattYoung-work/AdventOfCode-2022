def get_tail(hx,hy,tx,ty):
  d = {(0,0):(0,0), (0,1):(0,0), (1,1):(0,0), (1,0):(0,0), (1,-1):(0,0), \
       (0,-1):(0,0), (-1,-1):(0,0), (-1,0):(0,0), (-1,1):(0,0), (2,0):(1,0), \
       (2,1):(1,1), (2,2):(1,1), (1,2):(1,1), (0,2):(0,1), (-2,1):(-1,1), \
       (-2,2):(-1,1), (-1,2):(-1,1), (-2,0):(-1,0),(-2,-1):(-1,-1), (-2,-2):(-1,-1), \
       (-1,-2):(-1,-1), (0,-2):(0,-1), (2,-1):(1,-1), (2,-2):(1,-1), (1,-2):(1,-1)}
  a = hx - tx
  b = hy - ty
  dtx, dty = d[(a,b)]
  return (tx + dtx, ty + dty)

hx = 0
hy = 0
tail = [[0,0] for i in range(10)]

grid = [['.' for x in range(25)] for y in range(21)]

t_coords = {'0,0':1}

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
      tail[0][0],tail[0][1] = hx,hy
      for i in range(1,10):
        tail[i][0],tail[i][1] = get_tail(tail[i-1][0],tail[i-1][1], tail[i][0], tail[i][1])
      t_coords[(str(tail[9][0])+','+str(tail[9][1]))] = 1

print(len(list(t_coords)))