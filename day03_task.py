##### 과제 1 #####
'''
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
        is_prime = True

        if number < 2:
            print(f'{number} is not prime number')
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(f'{number} is prime number')
            else:
                print(f'{number} is not prime number')
    elif menu == '4':
        numbers = input("Input First Second number : ").split()
        n1, n2 = int(numbers[0]), int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1
        # numbers = [int(n) for n in numbers]
        # n1, n2 = min(numbers), max(numbers)

        is_prime = True
        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                pass
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(number, end=' ')
        print()
    elif menu == '5':
        print("Terminate program")
        break
    else:
        print("choose number 1 ~ 5!")
'''

##### 과제 2_6-1 #####
'''
# 6-1 ver.1
num = list(range(4))
num.sort(reverse=True)
for n in num :
    print(n, end=' ')

# 6-1 ver.2
n = 3
for i in range(n+1) :
    print(n-i, end=' ')

# 6-1 ver.3
for i in range(3,-1,-1):
    print(i, end=' ')
'''
##### 과제 2_6-2 #####
'''
guess_me = 7
number = 1

while True :
    if number < guess_me :
        print('too low')
    elif number == guess_me :
        print('found it!')
        break
    else :
        print('opps')
        break
    number += 1
'''
##### 과제 2_6-3 #####
'''
guess_me = 5

for number in range(10) :
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('opps')
        break
'''