
import sys
sys.stdin = open("input.txt",'rt')


a = 0
def reverse(x):
    x = list(map(int,str(x)))
    x.reverse()
    num = x
    global s
    for j in num:
        
        if num[0] == 0:
            num = num[1:]    
            
    return num


def isPrime(x):
    s = ''.join(map(str,x))
    a = int(s)
    
    for i in range(2,a):
        if a % i == 0:
            break
        
    else:
        return s



N = int(input())
nums = list(map(int,input().split()))
fs = []

for n in nums:
    reverse_num = reverse(n)
    Prime = isPrime(reverse_num)
    fs.append(Prime)
    fs = list(filter(None,fs))
    while '1' in fs:
        fs.remove('1')
print(' '.join(fs))
    
    



   

        
