T = int(input())
sum = 0
a = []

for i in range(1,T+1):
  A,B = input().split()
  A = int(A)
  B = int(B)
  sum = A+B
  a.append(sum)
for i in range(T):
  jh = a[i]
  print('Case #%d: %d'%(i+1,jh))
 
   

  


