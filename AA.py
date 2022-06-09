import sys
sys.stdin = open("input.txt",'rt')



N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]
nums.insert(0,[0]*N)
nums.append([0]*N)
for x in nums:
    x.insert(0,0)
    x.append(0)
cnt = 0
for i in range(1,len(nums)-1):
    for j in range(1,len(nums)-1):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        result = []
        for k in range(4):
            a = nums[i+dx[k]][j+dy[k]]
            result.append(a)
        if max(result)<nums[i][j]:
            cnt+=1
        
print(cnt)           