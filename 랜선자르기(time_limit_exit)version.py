import sys

sys.stdin = open("input.txt",'rt')

nums =[]
K,N = map(int,input().split())
for i in range(K):
    a = int(input())
    nums.append(a)

for i in range(1,min(nums)+1):
    row_list_sum=0
    for j in range(len(nums)):
        w = nums[j]//i
        row_list_sum += w
    if row_list_sum==N:
        q = float('-inf')
        if i>q:
            q = i
print(q)
            
    
        
    
        

  
    


    

   
    
        
   


       
        

        
   
