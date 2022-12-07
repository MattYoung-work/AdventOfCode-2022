def unique(sub):
  bar = [sub.count(x) for x in sub]
  return all([x==1 for x in bar])

index = 0

with open('input.txt','r') as f:
  stream = f.readline()
  
sub = stream[index:index+14]
while (not unique(sub)):
  index +=1
  sub = stream[index:index+14]

print(index+14)