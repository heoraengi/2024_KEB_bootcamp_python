'''
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
'''
####### 5장 텍스트 #######

# print('Give', "us", '''some''',"""space""")

'''
### 원시 문자열 사용 ###
univ = "Inha\nUniversity!"
print(univ)
#출력
# Inha
# University!

univ = r"Inha\nUniversity!"
print(univ)
#출력
# Inha\nUniversity! 그대로 출력!
'''
'''
### 문자열 연결 (+) ###
number1 = input("First number : ") # 7
number2 = input("Second number : ") # 4
print(number1+number2) # 74 # concatenation <- 두 입력을 문자로 받았기 때문에 11로 나오는 게 아니라 문자를 합친 74로 나온다.
'''
'''
### 복제하기 ###
print(number1 * 3) # 777 # 반복시킨다!
# print(number1 + 3) # 더하기는 숫자타입만 가능 # TypeError: can only concatenate str (not "int") to str
'''
'''
### 슬라이싱 ###
univ = "Inha\nUniversity!"
print(univ[:4]) # Inha
print(univ[:-11]) # Inha\n 까지 나옴
print(univ[:-12]) # Inha
print(univ[::2])
# Ih
#nvriy
'''
'''
### split() ###
# defalut 값은 ' '으로 되어있음
# 다른 구분점을 주고 싶으면 ()안에 원하는 값을 넣으면 됨
course = "2024 KEB BootCamp"
print(course)
list_course = course.split()
print(list_course)

course = "2024 KEB Bootcamp"
print(course)
list_course = course.split('B')
print(list_course)

# input구문을 두개 쓰지 않고 split을 활용해 한번에 받는다!
numbers = input("FirstNumber  SecondNumber : ").split() # 9 7
print(numbers[0]+numbers[1]) # 97 # concatenation
print(int(numbers[0])+int(numbers[1])) #16 # arithmetic operation : 산술 연산
'''

### join() ###
subjects = ['python', 'c++', 'database']
subjects_string = " / ".join(subjects)
print(subjects_string) # python / c++ / database