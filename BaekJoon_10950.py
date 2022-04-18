T = int(input())
a = []
for i in range(0,T) :
  A,B = input().split()
  A = int(A)
  B = int(B)
  sum = A + B
  a.append(sum)
print(*a,sep = '\n')
  

  