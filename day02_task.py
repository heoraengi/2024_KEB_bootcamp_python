# 과제 ) 예습문제
# 섭씨 화씨 프로그램에서 한번 알려주고 종료되지 않도록 반복문 사용하여 프로그램 작성
# 3번을 누르기 전에 1, 2번이 계속 돌아가도록 for문 or while문 사용
# **들여쓰기 주의
menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit    3) Quit program : ")

while(menu != '3') :
    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit :{fahrenheit}F, Celsius{((fahrenheit - 32.0) * 5/9):.2f}C')

    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius :{celsius}F, Fahrenheit{((celsius*9.0/5.0)+32):.2f}C')

    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit    3) Quit program : ")

print('Terminate Program')