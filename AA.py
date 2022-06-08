import sys
sys.stdin = open("input.txt",'rt')

N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]
ri = 0
harvest_list = []
summ = 0
for i in range(N):
    a = N//2
    if i <= a:
        harvest_list.append(nums[i][a-i:a+1+i])
    else:
        harvest_list.append(nums[i][i-a:2*a-ri])
        ri+=1


for i in range(N):
    a = sum(harvest_list[i])
    summ += a
print(summ)