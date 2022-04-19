N,X = input().split()
N = int(N)
X = int(X)
A = [0 for i in range(N)]
A = input().split()

for i in range(N):
  ai = A[i]
  ai = int(ai)
  if ai<X:
    print(A[i],end = ' ')
 
    

  