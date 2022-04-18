import sys
T = int(input())
sum = 0
a = []

for i in range(T):
  A,B = sys.stdin.readline().split()
  A = int(A)
  B = int(B)
  sum = A+B
  a.append(sum)
print(*a,sep = '\n')
  
  