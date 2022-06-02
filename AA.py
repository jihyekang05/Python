

import sys
#sys.stdin = open("input.txt",'rt')

N = int(input())
for i in range(N):
    a = input()
    a = a.lower()
    if a == a[::-1]:
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))