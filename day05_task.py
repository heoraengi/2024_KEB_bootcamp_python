# 9-1
def good() :
    """
    리스트 값 print 해주는 함수
    :return: 없음
    """
    print(['Harry', 'Ron', 'Hermione'])
good() # ['Harry', 'Ron', 'Hermione']

#9-2
def get_odds() -> list :
    """
    0~9의 숫자 중 홀수를 반환해주는 함수
    :return: list
    """
    odd_numbers = [i for i in range(10) if i%2==1]
    return odd_numbers
print(get_odds()[2]) # 5

#9-3
def test(func):
    def inner():
        print("start")
        print('Function Name : ',func.__name__)
        result= func()
        print('Result : ', result)
        print("end")
        # return result
    return inner

@test
def get_even() -> list :
    """
    0~9의 숫자 중 짝수를 반환해주는 함수
    :return: list
    """
    even_numbers = [i for i in range(10) if i%2==0]
    return even_numbers

get_even()
# 출력 결과
# start
# Function Name :  get_even
# Result :  [0, 2, 4, 6, 8]
# end

#9-4
class OopsException(Exception):
    pass

try :
    s = input('영단어를 입력하세요 : ')
    if s == 'oops' :
        raise OopsException
    print(f'입력하신 영단어는 {s} 입니다.')
except OopsException  :
    print('Caught as oops')
# 출력 결과
# Caught as oops
