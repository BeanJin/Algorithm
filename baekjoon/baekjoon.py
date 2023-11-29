# 10951

while True :
    try :
        a, b = map(int, input().split())
        c = a + b
        print(c)
    except :
        break

# 10807

count = 0
a = int(input())
b = input().split()

while True:
  if a == len(b):
    c = input()
    break

  else:
    b = input().split()

for i in b:
  if c == i:
    count += 1

print(count)

# 10871

n, x = map(int, input().split())

l1 = list(map(int, input().split()))

for i in range(n) :
    if l1[i] < x :
        print(l1[i], end = " ")
    else :
      continue

# 10818

n = int(input())

l1 = list(map(int, input().split()))

print(min(l1), max(l1))
2562
arr = []

for i in range(9) :
    a = int(input())
    arr.append(a)

maxarr = int(max(arr))
print(maxarr)

b = arr.index(maxarr)

print(b + 1)

# 10810

n, m = map(int, input().split())

l1 = [0] * (n + 1)

for a in range(m) :
  i, j, k = map(int, input().split())
  for b in range(i, j+1) :
    l1[b] = k

for c in range(1, len(l1)) :
  print(l1[c], end = ' ')# 10951

while True :
    try :
        a, b = map(int, input().split())
        c = a + b
        print(c)
    except :
        break

# 10807

count = 0
a = int(input())
b = input().split()

while True:
  if a == len(b):
    c = input()
    break

  else:
    b = input().split()

for i in b:
  if c == i:
    count += 1

print(count)

# 10871

n, x = map(int, input().split())

l1 = list(map(int, input().split()))

for i in range(n) :
    if l1[i] < x :
        print(l1[i], end = " ")
    else :
      continue

# 10818

n = int(input())

l1 = list(map(int, input().split()))

print(min(l1), max(l1))
2562
arr = []

for i in range(9) :
    a = int(input())
    arr.append(a)

maxarr = int(max(arr))
print(maxarr)

b = arr.index(maxarr)

print(b + 1)

# 10810

n, m = map(int, input().split())

l1 = [0] * (n + 1)

for a in range(m) :
  i, j, k = map(int, input().split())
  for b in range(i, j+1) :
    l1[b] = k

for c in range(1, len(l1)) :
  print(l1[c], end = ' ')

n, m = map(int, input().split())

l1 = []

for i in range(n):
    l1.append(i+1)

# 10813

for j in range(m) :
    a, b = map(int, input().split())
    c = l1[a-1]
    l1[a-1] = l1[b-1]
    l1[b-1] = c

print(*l1)

# 5597

l1 = [i for i in range(1, 31)]

for i in range(28) :
    n = int(input())

    l1.remove(n)

print(*l1, sep = "\n")

# 3052

for i in range(10) :
    n = int(input())

    l1.append(n % 42)

a = set(l1)

print(len(a))

# 10813

n, m = map(int, input().split())

l1 = [i for i in range(1, n+1)]

for j in range(m) :
    a, b = map(int, input().split())

    t = l1[a-1 : b]
    t.reverse()
    l1[a-1 : b] = t

print(*l1)

# 1546

n = int(input())
l1 = list((map(int, input().split())))
l2 = []
best = max(l1)

for i in l1 :
  l2.append(i / best * 100)

print(sum(l2) / n)

# 27866

s = input()
i = int(input())

print(s[i-1])

# 2743

s = input()

print(len(s))

# 9086

a = int(input())

for i in range(a) :
    b = input()
    print(b[0] + b[-1])

# 11654

a = input()

print(ord(a))

# 11720

n = int(input())
m = list(map(int, input()))

a = sum(m)

print(a)

# 10809

s = input()

l1 = []

for i in range(97, 123) :
    l1.append(chr(i))

for j in range(len(l1)) :
    print(s.find(l1[j]), end = " ")

# 2675

t = int(input())

for i in range(t) :
    r, s = input().split(" ")
    r = int(r)
    l1 = list(s)
    for j in range(len(l1)) :
        print(l1[j]* r, end = "")
    print()