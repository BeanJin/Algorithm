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