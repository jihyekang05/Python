import sys
sys.stdin = open("input.txt",'rt')

N = int(input())
a = [list(map(int,input().split())) for _ in range(N)]
cosum_list =[]
rosum_list = []
dae1 = []
dae2 = []
fin_dae1 = []
fin_dae2 = []

##세로합 구하기
for i in range(N):
    co_sum = 0
    for j in range(N):
        if j<(N-1):
            co_sum += a[j][i]
        elif j==(N-1):
            co_sum += a[j][i]
            cosum_list.append(co_sum)
##가로합 구하기
for i in range(N):
    ro_sum = 0
    for j in range(N):
       if j<(N-1):
           ro_sum += a[i][j]
       elif j ==(N-1):
           ro_sum += a[i][j]
           rosum_list.append(ro_sum)
##대각선 구하기
for i in range(N):
    dae1sum = 0
    dae1sum += a[i][i]
    dae1.append(dae1sum)
fin_dae1.append(sum(dae1))
##대각선 구하기
for i in range(N):
    dae2sum = 0
    dae2sum += a[i][N-i-1]
    dae2.append(dae2sum)
fin_dae2.append(sum(dae2))
##구한 리스트 합치기
fin_list = cosum_list+rosum_list+fin_dae1+fin_dae2
#리스트 내에 최대값 출력
print(max(fin_list))
