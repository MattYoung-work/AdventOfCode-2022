index = 0

with open('input.txt','r') as f:
  stream = f.readline()
  
sub = stream[index:index+4]
while (sub[0]==sub[1] or sub[0]==sub[2] or sub[0]==sub[3] or sub[1]==sub[2] or sub[1]==sub[3] or sub[2]==sub[3]):
  index +=1
  sub = stream[index:index+4]

print(index+4)