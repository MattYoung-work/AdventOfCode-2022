trees = []

with open('./input.txt','r') as f:
  for line in f:
    trees.append([x for x in line.rstrip()])


rows = len(trees)
cols = len(trees[0])

visible = [[False for x in range(cols)] for y in range(rows)]

#from right
for i in range(rows):
  for j in range(cols-1):
    visible[i][j] = (visible[i][j] or all([trees[i][j] > x for x in trees[i][j+1:]]))
  visible[i][-1] = True

#from left
for i in range(rows):
  for j in range(1,cols):
    visible[i][j] = (visible[i][j] or all([trees[i][j] > x for x in trees[i][:j]]))
  visible[i][0] = True
 
#from top
for j in range(cols):
  visible[0][j] = True
  for i in range(1,rows):
    visible[i][j] = (visible[i][j] or all([trees[i][j] > x for x in [trees[k][j] for k in range(i)]]))

#from bottom
for j in range(cols):
  visible[-1][j] = True
  for i in range(rows-1):
    visible[i][j] = (visible[i][j] or all([trees[i][j] > x for x in [trees[k][j] for k in range(i+1,rows)]]))

print(sum(x.count(True) for x in visible))