
import sys
sys.stdin = open("input.txt",'rt')


N,K = map(int,input().split())

##3중for문으로 리스트 내에 세가지 인자 더하기

arr = list(map(int,input().split()))
new_arr=[]
for i in range(0,len(arr)-2):
    for j in range(i+1,len(arr)-1):
        for k in range(j+1,len(arr)):
            s = arr[i]+arr[j]+arr[k]
            new_arr.append(s)


##리스트 내에 중복제거
result=[]

for value in new_arr:
    if value not in result:
        result.append(value)
result.sort(reverse=True)

##K번째 인자 
print(result[K-1])








  
    
    
   
