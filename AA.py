
import sys
sys.stdin = open("input.txt",'rt')

N,K = map(int,input().split())
s = []
for i in range(1,N+1):
    if N % i == 0:
        s.append(i)
if len(s)<K:
    print(-1)
else:
    print(s[K-1])