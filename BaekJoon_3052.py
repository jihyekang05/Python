a = []
b = []
for i in range (10):
  n = int(input())
  a.append(n)
for i in range (10):
  s = (a[i]%42)
  b.append(s)
c = set(b)
print(len(c))