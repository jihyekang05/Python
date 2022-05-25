
import sys
sys.stdin = open("input.txt",'rt')

N = int(input())
nums = list(map(int,input().split()))
max_sum = float('-inf')
max_num = 0

def digit_sum(x):
    sum = 0
    for i in str(x): 
       sum += int(i)
    return sum  

for x in nums:
    tot_sum=digit_sum(x)
    if tot_sum > max_sum:
        max_sum = tot_sum
        max_num = x

print(max_num)












