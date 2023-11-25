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