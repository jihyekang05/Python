N = int(input())
nums = list(map(int,input().strip()))
sum = 0
for i in range (0,N):
  sum += nums[i]
print(sum)