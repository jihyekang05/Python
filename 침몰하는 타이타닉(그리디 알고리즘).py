

import sys
sys.stdin=open("input.txt", "r")


N,M = map(int,input().split())

weight = list(map(int,input().split()))

weight.sort(reverse = True)
a = len(weight)-1
cnt = 0

for i in range(len(weight)):
    if weight[i]+weight[a] > M and a>=i:
        cnt += 1
        
       
    elif weight[i]+weight[a]<= M and a>=i:
        cnt += 1
        a -= 1
    else:
        break;
        
print(cnt)     
    





 
