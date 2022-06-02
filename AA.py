

import sys
sys.stdin = open("input.txt",'rt')

N = input()
a = []
cnt = 0
d = []
for i in range(len(N)):
    if N[i].isdigit() == True:
        a.append(N[i])


for j in range(len(a)):
    if a[j] == '0':
        d = a[j+1:]
    else:
        d = a[j:]
        break

d = ''.join(d)
b = int(d)
for i in range(1,b+1):
    if b % i == 0:
        cnt += 1
    else:
        pass
print(d)
print(cnt)