#    [H]         [H]         [V]    
#    [V]         [V] [J]     [F] [F]
#    [S] [L]     [M] [B]     [L] [J]
#    [C] [N] [B] [W] [D]     [D] [M]
#[G] [L] [M] [S] [S] [C]     [T] [V]
#[P] [B] [B] [P] [Q] [S] [L] [H] [B]
#[N] [J] [D] [V] [C] [Q] [Q] [M] [P]
#[R] [T] [T] [R] [G] [W] [F] [W] [L]
# 1   2   3   4   5   6   7   8   9 
#

stacks = [[''],['R','N','P','G'],['T','J','B','L','C','S','V','H'],['T','D','B','M','N','L'],\
  ['R','V','P','S','B'],['G','C','Q','S','W','M','V','H'],['W','Q','S','C','D','B','J'],\
  ['L','Q','F'],['W','M','H','T','D','L','F','V'],['L','P','B','V','M','J','F']]

with open('./input.txt','r') as f:
  for line in f:
    words = line.rstrip().split(' ')
    foo = []
    for num in range(int(words[1])):
      foo.append(stacks[int(words[3])].pop())
    for x in foo[::-1]:
      stacks[int(words[5])].append(x)
print(''.join(x[-1] for x in stacks))