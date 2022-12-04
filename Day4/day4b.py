sum = 0
with open('./input.txt','r') as f:
  for line in f:
    a, b = line.rstrip().split(',')
    a_min, a_max = a.split('-')
    b_min, b_max = b.split('-')
    a_min = int(a_min)
    a_max = int(a_max)
    b_min = int(b_min)
    b_max = int(b_max)
    if(((a_min <= b_min) and (a_max >= b_min)) or ((a_min >= b_min) and (a_min <= b_max))):
      sum += 1
print(sum)