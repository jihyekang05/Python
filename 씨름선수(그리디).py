
import sys
sys.stdin=open("input.txt", "r")


            

n = int(input())
spec = []
for i in range(n):
    h,w = map(int,input().split())
    spec.append((h,w))
spec.sort(reverse=True)

cnt = 0
mh = 0
mw = 0
for h,w in spec:
    if mh <= h:
        cnt += 1
        mh = h
        mw = w
    else:
        if mw<w:
            mw = w
            mh = h
            cnt+=1
        else:
            pass
print(cnt)
          
