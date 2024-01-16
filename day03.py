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


### 원시 문자열 사용 ###
'''
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

### 문자열 연결 (+) ###
'''
number1 = input("First number : ") # 7
number2 = input("Second number : ") # 4
print(number1+number2) # 74 # concatenation <- 두 입력을 문자로 받았기 때문에 11로 나오는 게 아니라 문자를 합친 74로 나온다.
'''

### 복제하기 ###
'''
print(number1 * 3) # 777 # 반복시킨다!
# print(number1 + 3) # 더하기는 숫자타입만 가능 # TypeError: can only concatenate str (not "int") to str
'''

### 슬라이싱 ###
'''
univ = "Inha\nUniversity!"
print(univ[:4]) # Inha
print(univ[:-11]) # Inha\n 까지 나옴
print(univ[:-12]) # Inha
print(univ[::2])
# Ih
#nvriy
'''

### split() ###
'''
# defalut 값은 ' '으로 되어있음
# 다른 구분점을 주고 싶으면 ()안에 원하는 값을 넣으면 됨
course = "2024 KEB BootCamp"
print(course)
list_course = course.split()
print(list_course) # ['2024', 'KEB', 'BootCamp']

course = "2024 KEB Bootcamp"
print(course)
list_course = course.split('B')
print(list_course) # ['2024 KE', ' ', 'ootcamp']

# input구문을 두개 쓰지 않고 split을 활용해 한번에 받는다!
numbers = input("FirstNumber  SecondNumber : ").split() # 9 7
print(numbers[0]+numbers[1]) # 97 # concatenation
print(int(numbers[0])+int(numbers[1])) #16 # arithmetic operation : 산술 연산
'''

### join() ###
'''
subjects = ['python', 'c++', 'database']
subjects_string = " / ".join(subjects)
print(subjects_string) # python / c++ / database
'''

### replace() ###
'''
course = "2024 KEB BootCamp"
print((course.replace('KEB','Inha'))) # 2024 Inha BootCamp
print(course) # 2024 KEB BootCamp
course = course.replace('KEB','Inha')
print(course) # 2024 Inha BootCamp # assignment 가능 # 전체를 바꾸는 건 가능하다!

course = "KEB 2024 KEB BootCamp KEB"
print(course) # KEB 2024 KEB BootCamp KEB
course1 = course.replace('KEB','Inha')
print(course1) # Inha 2024 Inha BootCamp Inha
course2 = course.replace('KEB','Inha',2) # count인수를 통해 원하는 개수만큼만 바꿀 수 있다.
print(course2) # Inha 2024 Inha BootCamp KEB
'''

### strip() ###
'''
course = " KEB 2024# !KEB BootCamp KEB...*!#"
print(course) # KEB 2024# !KEB BootCamp KEB...*!#
print(course.strip()) #KEB 2024# !KEB BootCamp KEB...*!#
course = "* KEB 2024# !KEB BootCamp KEB...*!#"
print(course) #* KEB 2024# !KEB BootCamp KEB...*!#
print(course.strip()) #* KEB 2024# !KEB BootCamp KEB...*!#
# 양끝에 공백이 없으므로 strip을 해도 변화가 없음!
print(course.strip("!#.*")) # KEB 2024# !KEB BootCamp KEB
'''

### find(), index() ###
'''
course = "* KEB 2024# KEB !BootCamp KEB...*!#"
print(course.find('KEB')) # 2 <- 앞에서부터 찾은 KEB의 첫번째 글자 인덱스 반환
print(course.rfind('KEB')) # 26  <- 뒤에서부터 찾은 KEB의 첫번째 글자 인덱스 반환
print(course[2]) # K
print(course[26]) # K
print(course.index('KEB')) # find랑 동일
print(course.rindex('KEB')) # rfind랑 동일
print(course.find('Inha')) # -1 # 찾는 값이 없으면 -1 리턴
# print(course.index('Inha')) # ValueError: substring not found
# index 함수는 값는 값이 없으면 예외를 던진다.

# find를 이용한 if문 예제
subjects="python c++ database linux"
subject = input("수강신청과목 입력 : ")
if subjects.find(subject) != -1 :
    print(f'해당 과목은 존재합니다. 위치는 {subjects.find(subject)}번 인덱스입니다.')
else :
    print("해당 과목이 존재하지 않습니다.")

# index 예외처리
subjects="python c++ database linux"
subject = input("수강신청과목 입력 : ")
try :
    print(f'해당 과목은 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다.')
except ValueError :
    print("해당 과목이 존재하지 않습니다.")
'''
### isalnum() : 문자열이 알파벳이나 숫자로 이루어져있는지 확인 ###
'''
subjects="python c++ database linux"
print(subjects.isalnum()) # False
subjects="pythoncdatabaselinux"
print(subjects.isalnum()) # True
subjects="pythoncdata1231456baselinux"
print(subjects.isalnum()) # True
subjects="pythoncdata1231456!!!baselinux"
print(subjects.isalnum()) # False
'''

### 대소문자 ###
'''
subjects.capitalize() # 문장 맨 앞글자만 대문자
subjects.title() # 단어 앞글자만 대문자
subjects.upper() # 모두 대문자
subjects.lower() # 모두 소문자
subjects.swapcase() # 대문자 소문자 반대로
'''

### 문자 정렬 ###
'''
subjects.center(50) # 지정공간에서 문자열 중앙 정렬
subjects.ljust(50) # 지정공간에서 문자열 왼쪽 정렬
subjects.rjust(50) # 지정공간에서 문자열 오른쪽 정렬
'''

### 딕셔너리의 format() 출력 ###
'''
subjects = {'python' : 'kim', 'c++' : 'sung', 'data structure' : 'kim', 'database' : 'kang'}
print("{0[python]} {0[data structure]}".format(subjects)) # kim kim
# format이 가지고 있는게 0번밖에 없는데 거기서 키값을 가지고 해당 value값을 출력 한다!
'''

### prime number ###
number = int(input("Input number : "))
is_prime = True

if number < 2 :
    print(f'{number} is not prime number')
else :
    i = 2
    while i < number:
        if number % i == 0 :
            is_prime = False
            break
        i +=1

    if is_prime :
        print(f'{number} is prime number')
    else :
        print(f'{number} is not prime number')

