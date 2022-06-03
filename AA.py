

import sys
sys.stdin = open("input.txt",'rt')
cards = []
for i in range(1,21):
    a = i
    cards.append(a)

for i in range(10):
    a,b = map(int,input().split())
    for idx,value in enumerate(cards):
        if a!=b and a == 1 and a == idx+1:
            cards[0:b]=cards[b-1::-1]
        elif a == b and a == idx+1:
            break
        elif a!=b and a>=2 and a == idx+1:
            cards[a-1:b]=cards[b-1:a-2:-1]
        else:
            continue

cards_new = [str(a) for a in cards]
print(' '.join(cards_new))