import sys
sys.stdin=open("input.txt", "r")

def Count(l):
    cnt = 0
    com = 0
    for j in range(len(cage)):
        if j==0:
            cnt+=1
            com = cage[0]
        elif cage[j]-com>=l:
            cnt+=1
            com = cage[j]
        else:
            pass
    return cnt

N,C = map(int,input().split())
cage = []
for i in range(N):
    a = int(input())
    cage.append(a)
cage.sort()

largest = 0
lt = 1
rt = max(cage)
res = 0

while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)<C:
        rt = mid-1
    else:
        lt = mid+1
        res = mid
print(res)

    
