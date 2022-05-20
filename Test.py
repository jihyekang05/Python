msg = "It is Time"
print(msg.upper())
print(msg.lower())
tmp = msg.upper()
print(tmp.find('T'))
print(tmp.count('T'))
print(msg)
print(msg[:2])
print(msg[3:5])
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end = ' ')
print()


for x in msg:
    print(x, end=' ')
print()

##대문자만 출력
for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

##소문자만 출력
for x in msg:
    if x.islower():
        print(x, end=' ')
print()

##알파벳만 출력
for x in msg:
    if x.isalpha():
        print(x, end='')
print()

##아스키넘버 출력
tmp='AZ'
for x in tmp:
    print(ord(x))
print()
