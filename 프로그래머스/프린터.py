
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
        
        
        
        
 ##최종본       
priorities = [2,1,3,2]
location = 2
r=priorities
x = {location:priorities[location]}
temp=[]
cnt=0
k=location
answer=0

for i,value in enumerate(priorities):
    comp_num=r[0]
    if(location>0):
        location-=1
    else:
        location=len(priorities)-1
    for j in range(1,len(r)):
        if(len(r)>1 and comp_num<r[j]):
            r = r[1:] + r[:1]
            break
        elif(len(r)==1):
            break           
    if(max(r)==r[0] ):
        temp.append(r[0])
        cnt+=1
        r.pop(0)
    if(location==0):
        print(cnt)
        
        
##프로그래머스 최종본

def solution(priorities, location):
    answer = 0
    cnt=0
    for i,value in enumerate(priorities):
        comp_num=priorities[0]
        if(location>0):
            location-=1
        else:
            location=len(priorities)-1
        for j in range(1,len(priorities)):
            if(len(priorities)==1):
                break
            elif(len(priorities)>1 and comp_num<priorities[j]):
                priorities = priorities[1:] + priorities[:1]
                print("here!!", priorities)
                break
            else:
                print("else!!")
        if(max(priorities)==priorities[0] ):
            cnt+=1
            priorities.pop(0)
        if(location==0):
            answer=cnt
            return answer
    # for i, value in enumerate(priorities):
    #     comp_num=priorities[0]
    #     if(location>0):
    #         location-=1
    #     else:
    #         location=len(priorities)-1
    #     for j in range(1,len(priorities)):
    #         if(len(priorities) > 1 and comp_num < priorities[j]):
    #             priorities = priorities[1:] + priorities[:1]
    #             break
    #         elif(len(priorities)==1):
    #             break
    #     if(max(priorities)==priorities[0] ):
    #         cnt+=1
    #         priorities.pop(0)
    #     if(location==0):
            
        
                
    



    
        
        
       
        
        
            
        

        






    
