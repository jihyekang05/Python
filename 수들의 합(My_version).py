import sys
sys.stdin = open("input.txt",'rt')

N,M = map(int,input().split())
num_list = list(map(int,input().split()))
summ = 0
answer = 0

for i in range(N):
    for j in range(i+1,N+1):
        summ = sum(num_list[i:j])
        if summ == M:
            answer+=1
print(answer)
        
