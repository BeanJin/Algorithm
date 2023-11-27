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
