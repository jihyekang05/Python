progresses = [93,30,55]
speeds = [1,30,5]
n = 100
a=0
b=0
res=[]
answer=[]
cnt=0
m=1
for i in range(len(progresses)):
    a = n-progresses[i]
    b=a//speeds[i]
    c=a%speeds[i]
    if(c>0):
        b+=1
    res.append(b)


for i in range(3):
    if(res[i]>m):
        m=res[i]
        cnt+=1
    else:
        cnt+=1
        answer.append(cnt)
        cnt=0
        m=1


print(answer)




