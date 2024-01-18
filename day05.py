### dict comprehension
'''
univ = 'inha university'
counts_alphabet = {letter:univ.count(letter) for letter in univ}
print(counts_alphabet)
# {'i': 3, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

univ = 'inha university'
counts_alphabet = dict()
for letter in univ :
    counts_alphabet[letter] = univ.count(letter)
print(counts_alphabet)
# {'i': 3, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

#8-10
squares = {i:i*i for i in range(10)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
'''

##### 9장 함수 ######
### 구간 소수 판정 프로그램 함수화###
'''
def is_prime(n) -> bool :
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean type으로 return
    :param n: 판정할 매개변수
    :return: 소수면 True, 아니면 False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n :
            if n % i == 0:
                return False
            i += 1
    return True

# help(is_prime) # 함수에 대한 설명 출력
# print(is_prime.__doc__) # help 없이 .__doc__로 출력 가능

numbers = input("Input First Second number : ").split()
n1, n2 = int(numbers[0]), int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2 + 1):
    if is_prime(number):
        print(number, end=' ')
'''

### 섭씨화씨소수 메뉴 함수 추가 ###
'''
def is_prime(n) -> bool :
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean type으로 return
    :param n: 판정할 매개변수
    :return: 소수면 True, 아니면 False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n :
            if n % i == 0:
                return False
            i += 1
    return True

while True :
    menu = input("1) Fahrenheit -> Celsius  2) Fahrenheit -> Celsius 3) Prime number 4) Range Prime number  5) Quit program : ")

    if menu =='1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(
            f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
        # .2f로 소수점 2번쨰자리까지 출력 (f스트링 서식)
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    elif menu == '3':
        number = int(input("Input number : "))

        if is_prime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is not prime number')
    elif menu == '4':
        numbers = input("Input First Second number : ").split()
        n1, n2 = int(numbers[0]), int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if is_prime(number):
                print(number, end=' ')
        print()
    elif menu == '5':
        print("Terminate program")
        break
    else:
        print("choose number 1 ~ 5!")
'''
### 파이썬은 다른 객체지향 언어와 다르게 오버로딩이 안됨 ###
'''
def a (n1,n2):
    print(n1,n2)

def a(n):
    print(n)

a(7)
a(7,11) # TypeError: a() takes 1 positional argument but 2 were given
'''
# None, True, False
'''
def a(n):
    if n is None:
        print(f'{n} is None')
    elif n :
        print(f'{n} is True')
    else :
        print(f'{n} is False')

a(None) # None is None
a('') #  is False
a(-9) # -9 is True
a([]) # [] is False
a([0]) # [0] is True
a(0) # 0 is False
'''

### 함수를 매개변수로 사용하기 ###
'''
def squares(n):
    return n*n

def run_function(f, number):
    return f(number)

print(squares(7))
print(run_function(squares, 9))
'''
def squares(*n) -> list:
    """
    넘겨받은 튜플 데이터를 거듭제곱하는 함수
    :param n: tuple
    :return: list
    """
    return [pow(i,2) for i in n]

def run_function(f, *number) -> list:
    return f(*number)

print(squares(7,5,2))
print(run_function(squares, 9,5,2))
