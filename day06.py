'''
def good():
    """
    chapter 9 thing to do. 9-1
    :return: list
    """
    harry_porter = input().split()
    return harry_porter

print(good())
'''
import random

'''
def get_odds(n) -> int:
    """
    1~n까지의 홀수를 발생시키는 제너레이터
    :param n: int
    :return: int
    """
    for i in range(1, n+1, 2):
        yield i

cnt = 0
odds = get_odds(9)
for odd in odds:
    cnt+=1
    if cnt == 3:
        print(f'Third number is {odd}') # Third number is 5
        break
'''

'''
def test(f) :
    """
    데코레이터 함수 : 시작하면 start 출력, 끝나면 end 출력
    :param f: function
    :return: closer function
    """
    #def test_in(*args, **kwargs):
    def test_in():
        print('start')
        f()
        print('end')
        # return result
    return test_in

@test
def greeting():
    print("안녕하세요!!!")

greeting()
'''
'''
# 반복문 사용
def factorial_repetition(n)-> int:
    """
    반복문으로 만든 팩토리얼 함수
    :param n:
    :return:
    """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

def factorial_recursion(n):
    """
    재귀함수를 사용한 팩토리얼 함수
    :param n: int
    :return: function, int
    """
    if n == 1 :
        return n
    else :
        return n * factorial_recursion(n-1)

number = int(input("number : "))
print(factorial_repetition(number))
print(factorial_recursion(number))
print(globals())
# 반복문은 속도가 빠름
# 대신 재귀함수는 변수를 줄일 수 있음 :  side_effect을 막을 수 있음
'''
'''
import random
# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1,100))
#
# print(numbers)

class OopsException(Exception):
    pass

numbers =  [random.randint(1,100) for _ in range(5)]
print(numbers)

try :
    pick = int(input(f'Input index ( 0 ~ {len(numbers)-1} ): '))
    print(numbers[pick])
    print(5/2)
    raise OopsException("!Oops!") # 예외 강제로 발생
except IndexError as err:
    print(f"Out of range : Wrong index number\n{err}")
except ValueError as err:
    print(f"Input only Number\n{err}")
except ZeroDivisionError as err :
    print(f'The denominator cannot be 0.\n{err}')
except OopsException as err:
    print(f'Oops Oops {err}')
except Exception as err : # 모든 에러 다 잡아줌. 그래서 이건 맨 마지막에 넣어줘야 함
    print(f"Error occurs\n{err}")
else :
    print(f'Program terminate')
'''
'''
def desc():
    def wrapper():
        print('w')
    print('a')
    return wrapper
desc() # a
# wrapper 함수에 던져진게 없으므로 나오는게 없음 그래서 'w' 출력 안됨

def desc(f):
    def wrapper():
        print('w')
        f()
    #print('a')
    return wrapper
def something():
    print('do something')

d = desc(something)
d()
# 출력결과
# w
# do something
'''

########## 객체 ##########
'''
class Pokemon:
    def __init__(self, name): # 이거 안에 new()가 있음
        self.name = name
        print(f"{name} : 포켓몬스터 생성")

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
charizard = Pokemon("리자몽")
charizard.attack(squirtle)
# 출력 결과
# 피카츄 : 포켓몬스터 생성
# 꼬부기 : 포켓몬스터 생성
# 리자몽 : 포켓몬스터 생성
# 리자몽 이(가) 꼬부기 을(를) 공격!
'''
'''
# 객체 지향 설계 원칙 중 리스코프 치환 원칙 :  서브 타입은 언제나 기반(부모) 타입으로 교체할 수 있어야 한다는 원칙
class Pokemon : # 부모 클래스
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

class Pikachu(Pokemon): # is-a 관계(=상속관계) # 자식 클래스
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")

    def electric_info(self):
        print("전기 계열의 공격을 합니다.")

class Squirtl(Pokemon):
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 물대포 공격!")

class Agumon:
    pass

p1 = Pikachu('피카츄','전기')
p2 = Squirtl('꼬부기')
p3= Pokemon("아무개")
p1.attack(p2) # 피카츄이(가) 꼬부기을(를) 전기 공격!
print(p1.name,p1.type)
'''
'''
class Animal:
    def says(self):
        return 'I speak'

class Horse(Animal):
    def says(self):
        return '말소리~'
class Donkey(Animal):
    def says(self):
        return '나귀소리~'

class Mule(Donkey,Horse):
    pass
    # def says(self):
    #     return '노새 노새~'
class Hinny(Horse,Donkey):
    # pass
    def says(self):
        return '버새 버새~'

m1 = Mule()
print(m1.says()) # 나귀소리~

h1 = Hinny()
print(h1.says()) # 버새 버새~
print(Hinny.__mro__) # 족보의 우선순위를 보여줌
# (<class '__main__.Hinny'>, <class '__main__.Horse'>, <class '__main__.Donkey'>, <class '__main__.Animal'>, <class 'object'>)
# 자기자신 - 첫번째 상속 - 두번째 상속 - 상속받은 클래스의 부모 클래스
'''
'''
class FlyingMixin:
    def fly(self):
        return f'{self.name}이(가) 날다~'

class SwimmingMixin:
    def swim(self):
        return f'{self.name}이(가) 수영을 합니다~'

class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self):
        print('공격!')

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados('갸라도스')
c1 = Charizard('리자몽')
print(g1.swim()) # 갸라도스이(가) 수영을 합니다~
print(c1.fly()) # 리자몽이(가) 날다~
c1.attack()
# Charizard.attack() # self가 와줘야하니깐 괄호 안에 괄호 안에 들어가줘야 함
Charizard.attack(c1)
'''

class FlyingMixin:
    def fly(self):
        return f'{self.name}이(가) 날다~'

class SwimmingMixin:
    def swim(self):
        return f'{self.name}이(가) 수영을 합니다~'

class Pokemon:
    def __init__(self, name):
        self.hidden_name = name
    def attack(self):
        print('공격!')
    def get_name(self):
        print("inside getter")
        return self.hidden_name
    def set_name(self, new_name):
        print("insid setter")
        self.hidden_name = new_name

    name = property(get_name, set_name)

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados('갸라도스')
c1 = Charizard('리자몽')
# print(g1.name) # 갸라도스
# g1.name = "잉어킹"
# print(g1.name) # 잉어킹
# print(g1.get_name())
# # inside getter
# # 갸라도스
# g1.set_name("잉어킹")
# # insid setter
# print(g1.get_name())
# # inside getter
# # 잉어킹
print(g1.name)
g1.name = "잉어킹"
print(g1.name)
# inside getter
# 갸라도스
# insid setter
# inside getter
# 잉어킹