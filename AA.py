import sys
sys.stdin = open("input.txt",'rt')

N = int(input())
first = list(map(int,input().split()))
M = int(input())
second = list(map(int,input().split()))

third = first+second
third.sort()
fin = [str(a) for a in third]
print(' '.join(fin))