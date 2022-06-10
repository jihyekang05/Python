import sys
sys.stdin = open("input.txt",'rt')

nums = [list(map(int,input().split())) for _ in range(7)]

cnt = 0
        
for q in range(7):
    s = [v[q] for v in nums]
    for i in range(len(s)+1):
        for j in range(3+i,len(s)+1):
            a = s[i:j]
            if len(a)==5:
                for k in range(1,3):
                    if k<2:
                        if a[2-k]==a[2+k]:
                            continue
                        else:
                            break
                    else:
                        if a[2-k]==a[2+k]:
                            cnt+=1
for s in range(7):
    n = nums[s]
    for i in range(len(n)+1):
        for j in range(3+i,len(n)+1):
            a = n[i:j]
            if len(a)==5:
                for k in range(1,3):
                    if k<2:
                        if a[2-k]==a[2+k]:
                            continue
                        else:
                            break
                    else:
                        if a[2-k]==a[2+k]:
                            cnt+=1
print(cnt)
