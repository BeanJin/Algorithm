# 3003

c1 = [*map(int, input().split())]
c2 = [1, 1, 2, 2, 2, 8]
l1 = []

for i in range(6) :
    l1.append(c2[i] - c1[i])

print(*l1)

# 2444

n = int(input())

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

for j in range(n-1, 0, -1) :
    print(' ' * (n-j) + '*' * (2*j-1))

# 10998

a = input()

b = ''.join(reversed(a))

if a == b :
    print('1')

else :
    print('0')

# 1157

a = input().lower()
l1 = list(set(a))
c = []

for i in l1 :
    cc = a.count(i)
    c.append(cc)

if c.count(max(c)) >= 2 :
    print('?')
else :
    print(l1[(c.index(max(c)))].upper())

