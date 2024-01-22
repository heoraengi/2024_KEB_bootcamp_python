class FlyingMixin:
    def fly(self):
        return f'{self.__name}이(가) 날다~'

class SwimmingMixin:
    def swim(self):
        return f'{self.__name}이(가) 수영을 합니다~'
class Pokemon:
    def __init__(self, name):
        self.__name = name
    def attack(self):
        print('공격!')
    @property
    def name(self):
        # print("inside getter")
        return self.__name
    @name.setter
    def name(self, new_name):
        # print("insid setter")
        self.__name = new_name

    # 매직메소드
    # 원래 객체를 그냥 print 하면 객체 이름이 아니라 객체 주소가 출력된다.
    # 해당 함수를 통해서 내가 원하는 방식으로 출력이 가능한다.
    def __str__(self):
        return self.__name + "입니다"

    def __add__(self,target):
        return self.__name + " + " + target.__name

    # name = property(get_name, set_name)

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados('갸라도스')
c1 = Charizard('리자몽')
print(g1)
print(c1)
print(g1+c1)