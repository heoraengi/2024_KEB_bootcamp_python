####### 2장 데이터 #######
'''
print(0.1, 1e-1)
print(0.01, 1e-2)
print(314.865, 0.341865e3) # e 지수 표현
print(21000, 21_000) # _ 천단위 구분용

univ = "Inha university"
print(univ) # 출력 : Inha university
print(univ[5]) # 출력 : u
# univ[5] = 'U' # 에러발생 : str형태는 immutable이라서 값 변경 불가능

subjects = ['a', 'b', 'c', 'd', 'e']
print(subjects) # 출력 : ['a', 'b', 'c', 'd', 'e']
print(subjects[3]) # 출력 : d
print(subjects[3:4]) # 출력 : ['d']
subjects[3] = 'f'
print(subjects[3]) # 출력 : f # mutable이라서 값 변경 가능
'''

# literal 정수는 변수가 아닌 값 그 자체를 말함; 데이터 그 자체임
# python console에 help("keywords") 실행하면 키워드가 나옴
# 변수명 생성 시 키워드 불가, 숫자로 시작 불가, 특수기호는 _만 가능

### 할당 ###
'''
x = 2
y = x + 5
print(y)

print(type(3.14))
print(type(3.14) == float) # True
print(isinstance(3.14, float)) # True
print(isinstance("inha", float)) # False
print(isinstance(55, float)) # False
'''
### 복사 ###
'''
artists = ['BTS', 'NewJeans', 'RISE', 'SES']
groups = artists
print(artists, groups)
# ['BTS', 'NewJeans', 'RISE', 'SES'] ['BTS', 'NewJeans', 'RISE', 'SES']
artists[3] = 'aespa'
print(artists, groups)
# ['BTS', 'NewJeans', 'RISE', 'aespa'] ['BTS', 'NewJeans', 'RISE', 'aespa']
# groups 변수는 artists 변수를 참조했으므로 서로 같은 주소를 바라보고 있어 artists가 바끼면 groups도 바뀐다.
'''

####### 3장 숫자 #######
'''
money = 3,000,000 # 쉼표를 사용하면 변수타입이 tuple로 됨
print(money) # (3, 0, 0)
print(type(money)) # <class 'tuple'>

cash = 3_000_000
print(cash) # 3000000
print(type(cash)) # <class 'int'>
'''

### 입력 및 연산 및 출력 ###
'''
base_number = int(input('Input base number : '))
exponent_number = int(input('Input exponent number : '))
# f-string
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {pow(base_number, exponent_number)}')

# format function
print('밑은 {0}, 지수는 {1} 결과 값은 {2}'.format(base_number,exponent_number,pow(base_number, exponent_number)))
print('밑은 {}, 지수는 {} 결과 값은 {}'.format(base_number,exponent_number,pow(base_number, exponent_number))) # 순서대로 입력하는 거면 숫자 안넣어도 됨

# c like
print('밑은 %d, 지수는 %d, 결과 값은 %d' % (base_number,exponent_number,pow(base_number, exponent_number)))

first_number = int(input('First number : '))
second_number = int(input('Second number : '))
quotient = first_number // second_number
remainder = first_number % second_number

print(f'몫은 {quotient}, 나머지는 {remainder}')
print(f'몫은 {divmod(first_number,second_number)[0]}, 나머지는 {divmod(first_number,second_number)[1]}')
'''
### 진수표현법 ###
'''
dec = 65
octal = 0o101
hexadecimal = 0x41
binary = 0b01000001
print(dec, octal, hexadecimal, binary) # 모두 65로 나옴
print(chr(binary)) # A <- 아스키코드로 변환
print(ord('A')) #  65 <- 숫자로 변환
'''

### 진수 변환 (int 이용) ###
'''
print(int('10', 2)) # 2
print(int('10', 8)) # 8
print(int('10', 16)) # 16
print(int('10', 22)) # 22
print(int('1A', 16)) # 26
'''

### 파이썬 정수 오버플로우 ###
'''
googol = 10**100
print(googol) # 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# 해당 변수는 이미 int가 담을 수 있는 공간을 넘어섰다.
# 대부분이 언어는 정수 오버플로우가 발생하겠지만 파이썬의 경우 문제없이 아주 큰 정수를 처리해준다.
# 값이 커질수록 메모리를 더 할당해주는 특징을 가지고 있다.
'''

####### 4장 if #######

### 화씨 -> 섭씨 변환기 ###
'''
# (0°F − 32) × 5/9 = -17.78°C
# (0°C × 9/5) + 32 = 32°F
menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit    3) Quit program : ")
if menu == '1':
    fahrenheit = float(input('Input Fahrenheit : '))
    print(f'Fahrenheit :{fahrenheit}F, Celsius{((fahrenheit - 32.0) * 5/9):.2f}C')

elif menu == '2':
    celsius = float(input('Input Celsius : '))
    print(f'Celsius :{celsius}F, Fahrenheit{((celsius*9.0/5.0)+32):.2f}C')

else :
    print('Terminate Program')
'''

### True or False ###
'''
# 0값이거나 원소가 존재하지 않는 것들은 False이다.
temp = [] # False # 빔
if temp : print("존재함")
else : print ('빔')

temp = [0] # True # 존재함
if temp : print("존재함")
else : print ('빔')
'''

### 여러개 비교하기 ###
# 자음 모음 찾기
letter = input('Input alphabet letter : ')
vowels = {'a', 'e', 'i', 'o', 'u'}
# vowels = "aeiou" # 문자열로도 가능!
print(type(vowels)) # <class 'set'>
if letter in vowels:
    print(f'{letter} is a vowel~')
else :
    print(f'{letter} is a consonant~')


