# Assignment(loop)
# (100℉ - 32) * 5/9 = 3.778℃
# (0°C × 9/5) + 32 = 32°F

while True :
    menu = input("1) Fahrenheit -> Celsius  2) Fahrenheit -> Celsius  3) Quit program : ")

    if menu =='1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(
            f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
        # .2f로 소수점 2번쨰자리까지 출력 (f스트링 서식)
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    elif menu == '3':
        print("Terminate program")
        break
    else:
        print("choose number 1 or 2 or 3!")