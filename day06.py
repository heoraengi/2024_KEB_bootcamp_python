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

