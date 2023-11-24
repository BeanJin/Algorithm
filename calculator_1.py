def add (a, b) :
    return a + b

def subtrack(a, b) :
    return a - b

def multiply(a, b) :
    return a * b

def divide(a, b) :
    if b == 0 :
        return " 이거 안된다잉 "
    return a / b

print('단순 계산기')
print('어떤거 할지 정하라')
print('1 : 덧셈')
print('2 : 뺄셈')
print('3 : 곱셈')
print('4 : 나눗셈')

while True :
    choice = input("선택( 1 / 2 / 3 / 4 )")

    if choice in('1', '2', '3', '4') :
        num1 = float(input('첫 번째 숫자 : '))
        num2 = float(input('두 번째 숫자 : '))

        if choice == '1' :
            print(num1, '+', num2, '=', add(num1, num2))
        
        elif choice == '2' :
            print(num1, '-', num2, '=', subtrack(num1, num2))

        elif choice == '3' :
            print(num1, '*', num2, '=', multiply(num1, num2))
        
        elif choice == '4' :
            print(num1, '/', num2, '=', divide(num1, num2))
        
        break

    else :
        print('단디 고르래이')
            