

import sys
sys.stdin = open("input.txt",'rt')

N = int(input())
result = list(map(int,input().split()))
cnt=[0]*N
val = 0
sum = 0
for idx,value in enumerate(result):
    if value == 1:
        val += 1
        cnt[val]+=1
    elif value == 0:
        val =0
       
    
for i,j in enumerate(cnt):
    a = i*j
    sum+=a
   
print(sum)
