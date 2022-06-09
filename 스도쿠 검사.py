import sys
sys.stdin = open("input.txt",'rt')

puzzle = [list(map(int,input().split())) for _ in range(9)]
cnt = 0



for i in range(3):
    for j in range(3):
        ch3 = [0]*10
        for k in range(3):
            for s in range(3):
                ch3[puzzle[i*3+k][j*3+s]]=1
        if sum(ch3)!=9:
            cnt+=1
        else:
            pass
for i in range(9):
    a = [w[i] for w in puzzle]
    q = set(a)
    if i<8 and len(q) == 9:
        continue
    elif len(q) != 9:
        cnt +=1
        break
    else:
        continue

for i in range(9):
    a = set(puzzle[i])
    if len(a)== 9:
        continue
    else:
        cnt+=1

if cnt>0:
    print('NO')
else:
    print('YES')        

        


        
