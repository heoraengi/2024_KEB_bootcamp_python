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

import random
# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1,100))
#
# print(numbers)

numbers =  [random.randint(1,100) for _ in range(5)]
print(numbers)

try :
    pick = int(input(f'Input index ( 0 ~ {len(numbers)-1} ): '))
    print(numbers[pick])
    print(5/0)
except IndexError as err:
    print(f"Out of range : Wrong index number\n{err}")
except ValueError as err:
    print(f"Input Only Number\n{err}")
except ZeroDivisionError as err :
    print(f'The denominator cannot be 0.\n{err}')
except Exception as err : # 모든 에러 다 잡아줌. 그래서 이건 맨 마지막에 넣어줘야 함
    print(f"Error occurs\n{err}")


