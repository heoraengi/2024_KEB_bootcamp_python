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
artists = ['BTS', 'NewJeans', 'RISE', 'SES']
groups = artists
print(artists, groups)
# ['BTS', 'NewJeans', 'RISE', 'SES'] ['BTS', 'NewJeans', 'RISE', 'SES']
artists[3] = 'aespa'
print(artists, groups)
# ['BTS', 'NewJeans', 'RISE', 'aespa'] ['BTS', 'NewJeans', 'RISE', 'aespa']
# groups 변수는 artists 변수를 참조했으므로 서로 같은 주소를 바라보고 있어 artists가 바끼면 groups도 바뀐다.


####### 3장 숫자 #######
money = 3,000,000 # 쉼표를 사용하면 변수타입이 tuple로 됨
print(money) # (3, 0, 0)
print(type(money)) # <class 'tuple'>

cash = 3_000_000
print(cash) # 3000000
print(type(cash)) # <class 'int'>

### 입력 및 연산 ###
base_number = int(input('Input base number : '))
exponent_number = int(input('Input exponent number : '))
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number**exponent_number}')