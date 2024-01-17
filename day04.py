### 개선시킨 Prime number ###
'''
# import math
numbers = input("Input First Second number : ").split()
n1, n2 = int(numbers[0]), int(numbers[1])
if n1 > n2 :
    n1, n2 = n2, n1

is_prime = True
for number in range(n1,n2+1) :
    is_prime = True

    if number < 2:
        pass
    else:
        i = 2
        # while i < math.sqrt(number)+1 :
        while i*i <= number :
            if number % i == 0:
                is_prime = False
                break
            i += 1
            # print(i, end=', ')
        if is_prime :
            print(number, end=' ')
'''

####### 7장 튜플과 리스트 #######
# 튜플은 꼭 콤마(,)가 있어야 함
# 괄호()는 선택사항이다.
'''
t1 = (5)
print(type(t1)) # <class 'int'>
t2 = 5,
print(type(t2)) # <class 'tuple'>
t3 = (5,)
print(type(t3)) # <class 'tuple'>
t4 = (5,7)
print(type(t4)) # <class 'tuple'>
t5 = 5,7
print(type(t5)) # <class 'tuple'>
t6 = "python", "kim" # packing
print(type(t6), t6[1]) # <class 'tuple'>  kim
subject, prof = t6 # unpacking
print(prof) # kim
print(subject) # python
# packing 개수보다 unpacking 시키려는 변수 개수가 더 많으면 에러 발생 / 서로 개수가 맞아야 함
# a, b, c = t6 # ValueError: not enough values to unpack
t7 = () # 빈 튜플은 콤마가 없어도 튜플임
print(type(t7)) # <class 'tuple'>
t8 = tuple()
print(type(t8)) # <class 'tuple'>

t9 = 1,2,3
t10 = 1,2,3,4
print(t9 == t10) # False
print(t9 <= t10) # True
print(t9 >= t10) # False

t9 = 1,2,3
t10 = 1,1,1,1
print(t9 == t10) # False
print(t9 <= t10) # False
print(t9 >= t10) # True

t11 = 4.43,
t12 = 3.97, 4.1, 3.2
print(t11 + t12) # (4.43, 3.97, 4.1, 3.2)
print(id(t11)) # 1714976284320
t11 = t11 + t12 # 할당된 후 아이디가 달라짐 <- 왜냐하면 튜플은 immutable 이기때문에 주소가 바뀜
print(t11) # (4.43, 3.97, 4.1, 3.2)
print(id(t11)) # 1714977045488
'''

### reverse() ###
'''
subjects = ["c++", "ptyhon", "java"]
# subjects.reverse() # 원복이 그대로 바뀜
subjects = subjects[::-1] # subjects.reserve()
print(subjects)
'''

### del, remove(), pop(), clear() ###
'''
subjects = ["c++","java", "ptyhon", "java"]
# subjects.remove("java") # 동일한 값이 있다면 이렇게 하면 제일 첫번째 나오는"java"만 지움
del subjects[3] # del 명령어를 이용해 원하는 걸 선택해서 지울 수 있음
print(subjects)
subjects.pop() # 숫자를 입력하지 않으면 제일 뒤에 있는 값이 빠져나옴
print(subjects)
subjects.clear() # 안에 있는 내용 전부 삭제
'''

### sort(), sorted() ###
# subjects = ["c++","java", "ptyhon", "java"]
# subjects = ["c++","java", 5,"ptyhon",7, "java"]
# list안에 type이 다르면 정렬 불가 ( 근데 int랑 float랑 같이 있는 건 됨)
'''
subjects = ["c++","데이터베이스","java", "5","ptyhon","7", "java"]
subjects.sort()
print(subjects) # ['5', '7', 'c++', 'java', 'java', 'ptyhon', '데이터베이스'] # 숫자 ,영어, 한글 순
subjects.sort(reverse=True)
print(subjects)
copy_subjects = sorted(subjects)
print(copy_subjects)
'''

### copy(), deepcopy() ###
'''
subjects = ["a", "b", "c"]
a = subjects # 할당이라서 subjects 변수랑 같은 곳을 가르킴
b = subjects.copy()
c = list(subjects)
d = subjects[:]
print(subjects,a,b,c,d) # ['a', 'b', 'c'] ['a', 'b', 'c'] ['a', 'b', 'c'] ['a', 'b', 'c'] ['a', 'b', 'c']
subjects[1] = "x"
print(subjects,a,b,c,d) # ['a', 'x', 'c'] ['a', 'x', 'c'] ['a', 'b', 'c'] ['a', 'b', 'c'] ['a', 'b', 'c']

subjects = ["a", ["b", "c"], "d"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
print(subjects,a,b,c,d)
# ['a', ['b', 'c'], 'd'] ['a', ['b', 'c'], 'd'] ['a', ['b', 'c'], 'd'] ['a', ['b', 'c'], 'd'] ['a', ['b', 'c'], 'd']
subjects[1][1] = "x" # <- 이렇게 mutable한 리스트 값을 바꾸기 때문에 전부 바뀜
print(subjects,a,b,c,d)
# ['a', ['b', 'x'], 'd'] ['a', ['b', 'x'], 'd'] ['a', ['b', 'x'], 'd'] ['a', ['b', 'x'], 'd'] ['a', ['b', 'x'], 'd']

import copy
subjects = ["a", ["b", "c"], "d"]
a = subjects
b = subjects.copy()
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(subjects)
print(subjects,a,b,c,d,e)
# ['a', ['b', 'c'], 'd'] ['a', ['b', 'c'], 'd'] ['a', ['b', 'c'], 'd'] ['a', ['b', 'c'], 'd'] ['a', ['b', 'c'], 'd'] ['a', ['b', 'c'], 'd']
subjects[1][1] = "x" # <- 이렇게 mutable한 리스트 값을 바꾸기 때문에 전부 바뀜
print(subjects,a,b,c,d,e)
# ['a', ['b', 'x'], 'd'] ['a', ['b', 'x'], 'd'] ['a', ['b', 'x'], 'd'] ['a', ['b', 'x'], 'd'] ['a', ['b', 'x'], 'd'] ['a', ['b', 'c'], 'd']
# deepcopy한 부분만 새로운 메모리를 할당 받아서 값이 변하지 않음
'''

### List Comprehension ###
'''
squares = [n*n for n in range(1,6)]
print(squares)

rows = list(range(1,4))
cols = list(range(1,3))
cells = [(row, col)for row in rows for col in cols]
print(cells) # [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)

thing = (n for n in range(1,6)) # 제너레이터 컴프리헨션
print(thing) # <generator object <genexpr> at 0x000001C99A0A9BD0>
'''
####### 8장 딕셔너리 #######
### dict ###
'''
sugang = dict(python='kim', cpp='sung', db='kang')
print(sugang)
sugang['datastructure'] = 'kim' # add
print(sugang)
sugang['datastructure'] = 'park' # update
print(sugang['db'])
print(sugang.get('db'))
print(sugang.get('opensource')) # None : 존재하지 않는 키를 넣으면 None이 나옴
print(sugang.get('opensource', 'no exist')) # no exist  # 옵션으로 문구를 넣을 수 있음
'''
# 3.6버전 이전 dict은 순서 개념이 없어서 랜덤하게 출력됐음
sugang = dict(python='kim', cpp='sung', db='kang')
for suject, professor in sugang.items() :
    print(f'{suject} 과목 담당교수는 {professor}입니다')

for k in sugang.keys(): # or for k in sugang.keys()
    print(k)

for v in sugang.values():
    print(v)

for s in sugang.items():
    print(s) # 튜플형태로 출력