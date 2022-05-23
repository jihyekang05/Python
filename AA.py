
import sys
sys.stdin = open("input.txt",'rt')


N,K = map(int,input().split())


arr = list(map(int,input().split()))
new_arr=[]
for i in range(0,len(arr)-2):
    for j in range(i+1,len(arr)-1):
        for k in range(j+1,len(arr)):
            s = arr[i]+arr[j]+arr[k]
            new_arr.append(s)



result=[]

for value in new_arr:
    if value not in result:
        result.append(value)
result.sort(reverse=True)
print(result[K-1])








  
    
    
   