
import sys
sys.stdin=open("input.txt", "r")


L = int(input())

nums = list(map(int,input().split()))

M = int(input())
nums.sort()


cnt = len(nums)-1
nmin = 0
nmax = 0

for i in range(M):
    nums[0] += 1
    nums[cnt] -= 1
    nums.sort()

res = max(nums)-min(nums)
print(res)
