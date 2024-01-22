# class FlyingBehavior:
#     def fly(self):
#         return f'하늘을 날다~'
#
# class JetPack(FlyingBehavior):
#     def fly(self):
#         return f'로켓추진기로 하늘을 날아갑니다.'
#
# class NoFly(FlyingBehavior):
#     def fly(self):
#         return f'하늘을 날 수 없습니다.'
# class FlyWithWings(FlyingBehavior):
#     def fly(self):
#         return f'날개로 하늘을 훨훨 날아갑니다.'
#
# class Swimming:
#     def swim(self):
#         return f'{self.__name}이(가) 수영을 합니다~'
# class Pokemon:
#     def __init__(self, name, hp, fly_behavior):
#         self.__name = name
#         self.hp = hp
#         self.fly_behavior = fly_behavior # aggregation(has-a)
#
#     def set_fly_behavior(self, fly):
#         self.fly_behavior = fly
#
#
#     def attack(self):
#         print('공격!')
#     @property
#     def name(self):
#         # print("inside getter")
#         return self.__name
#     @name.setter
#     def name(self, new_name):
#         # print("insid setter")
#         self.__name = new_name
#
#     # 매직메소드
#     # 원래 객체를 그냥 print 하면 객체 이름이 아니라 객체 주소가 출력된다.
#     # 해당 함수를 통해서 내가 원하는 방식으로 출력이 가능한다.
#     def __str__(self):
#         return self.__name + "입니다"
#
#     def __add__(self,target):
#         # return self.__name + " + " + target.__name
#         return  f'두 포켓몬스터 체력의 합은 {self.hp + target.hp}입니다.'
#
#
#
#     # name = property(get_name, set_name)
#
# class Charizard(Pokemon):
#     pass
#
# class Pikachu(Pokemon):
#     pass
#
# nofly = NoFly()
# p1 = Pikachu('피캬츄',100,nofly) # LSP
# wings= FlyWithWings()
# c1 = Charizard('리자몽',120, wings) # LSP
# print(c1.fly_behavior.fly())
# print(p1.fly_behavior.fly())
# p1.set_fly_behavior(JetPack())
# print(p1.fly_behavior.fly())

'''
class FlyingBehavior:
    def fly(self):
        return f'하늘을 날다~'

class JetPack(FlyingBehavior):
    def fly(self):
        return f'로켓추진기로 하늘을 날아갑니다.'

class NoFly(FlyingBehavior):
    def fly(self):
        return f'하늘을 날 수 없습니다.'
class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f'날개로 하늘을 훨훨 날아갑니다.'

class Pikachu:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        self.fly_behavior = NoFly() # composition


p1 = Pikachu('피캬츄',100) # LSP
print(p1.fly_behavior.fly())
'''
import mymath

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

        if mymath.is_prime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is not prime number')
    elif menu == '4':
        numbers = input("Input First Second number : ").split()
        n1, n2 = int(numbers[0]), int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if mymath.is_prime(number):
                print(number, end=' ')
        print()
    elif menu == '5':
        print("Terminate program")
        break
    else:
        print("choose number 1 ~ 5!")