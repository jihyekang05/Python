
import sys
#sys.stdin = open("input.txt",'rt')


N = int(input())
grades = list(map(int,input().split()))
sum = sum(grades)
average = round(float(sum/N))
min = float('inf')

for idx, x in enumerate(grades):
    min_sub = abs(x-average)
    if min_sub < min :
        index = idx+1
        closest_grade = x
        min = min_sub
        
    elif min_sub == min:
        if x>closest_grade:
            index = idx+1
            min = min_sub
            closest_grade = x
print(average,index)
        








  
    
    
   