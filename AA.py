import sys
sys.stdin = open("input.txt",'rt')

N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]
M = int(input())
rot = [list(map(int,input().split())) for _ in range(M)]
fin_list = []
summ = 0
for i in range(M):
    a = rot[i][0]
    b = rot[i][1]
    c = rot[i][2]%N
    if b == 0:
        nums[a-1]= nums[a-1][c:]+nums[a-1][0:c]
    else:
        nums[a-1] = nums[a-1][N-c:]+nums[a-1][0:N-c]

    
for i in range(N):
    a = N//2
    if N//2>=i:
        fin_list.append(nums[i][i:N-i])
    else:
        fin_list.append(nums[i][N-i-1:i+1])

for i in range(N):
    a = sum(fin_list[i])
    summ += a
print(summ)
