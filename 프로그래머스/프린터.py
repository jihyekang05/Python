
priorities = [1,1,9,1,1,1]
location = 0
r=priorities
x = {location:priorities[location]}
temp=[]
cnt=0
answer=0
for i in range(len(priorities)+1):
    comp_num = r[0]
    for j in range(1,len(r)):
        if(len(r)>1 and comp_num<r[j]):
            r = r[1:]+r[:1]
            break
        elif(len(r)==1):
            break
 
    if(max(r)==r[0]):
        temp.append(r[0])
        cnt+=1
        ##if(priorities[0]==x):
            ##print(cnt)
        if(r[0]==priorities[location]):
            print(cnt)
        r.pop(0)
        
       
        
        
            
        

        






    
