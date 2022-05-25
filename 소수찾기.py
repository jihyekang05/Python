import sys
sys.stdin = open("input.txt",'rt')
cnt=0

for i in range(2,int(input())+1):
    
    for j in range(2,i):
        if i % j == 0:
            break   
    else:
        cnt+=1
print(cnt)
