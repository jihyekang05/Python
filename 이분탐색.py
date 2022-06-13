import sys

sys.stdin = open("input.txt",'rt')


N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
for idx,value in enumerate(nums):
    if value == M:
        print(idx+1)
    else:
        continue
