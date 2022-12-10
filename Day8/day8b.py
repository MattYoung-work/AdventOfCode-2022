trees = []

with open('./input.txt','r') as f:
  for line in f:
    trees.append([x for x in line.rstrip()])


rows = len(trees)
cols = len(trees[0])

#create score grid
score = [[1 for x in range(cols)] for y in range(rows)]

#set edges
score[0] = [0 for x in score[0]]
score[-1] = [0 for x in score[-1]]
for x in range(rows):
  score[x][0] = 0
  score[x][-1] = 0


#looking up
for j in range(cols):
  for i in range(1,rows):
    dst = 1
    tmp = reversed([x for x in [trees[k][j] for k in range(i)]])
    for tr in tmp:
      if trees[i][j] > tr: dst += 1
      else: break
    else: dst -= 1 #error correction for going off the edge
    score[i][j] *= dst

#looking down
for j in range(cols):
  for i in range(1,rows):
    a = rows - i -1
    dst  = 1
    tmp = [x for x in [trees[k][j] for k in range(a+1,rows)]]
    for tr in tmp:
      if trees[a][j] > tr: dst += 1
      else: break
    else: dst -= 1
    score[a][j] *= dst

#looking left
for i in range(rows):
  for j in range(1,cols):
    dst = 1
    tmp = reversed(trees[i][:j])
    for tr in tmp:
      if trees[i][j] > tr: dst += 1
      else: break
    else: dst -= 1
    score[i][j] *= dst

#looking left
for i in range(rows):
  for j in range(cols-1):
    dst = 1
    tmp = trees[i][j+1:]
    for tr in tmp:
      if trees[i][j] > tr: dst += 1
      else: break
    else: dst -= 1
    score[i][j] *= dst


print(max([max(x) for x in score]))