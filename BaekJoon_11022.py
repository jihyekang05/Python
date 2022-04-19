import sys
T = int(input())
num_sum = []
a = []
b = []
for i in range(T):
  A,B = sys.stdin.readline().split()
  A = int(A)
  B = int(B)
  sum = A + B
  num_sum.append(sum)
  a.append(A)
  b.append(B)
for i in range(T):
  num = num_sum[i]
  print('Case #%d: %d + %d = %d'%(i+1,a[i],b[i],num))
  
  
  