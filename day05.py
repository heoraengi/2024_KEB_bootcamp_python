### dict comprehension
'''
univ = 'inha university'
counts_alphabet = {letter:univ.count(letter) for letter in univ}
print(counts_alphabet)
# {'i': 3, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

univ = 'inha university'
counts_alphabet = dict()
for letter in univ :
    counts_alphabet[letter] = univ.count(letter)
print(counts_alphabet)
# {'i': 3, 'n': 2, 'h': 1, 'a': 1, ' ': 1, 'u': 1, 'v': 1, 'e': 1, 'r': 1, 's': 1, 't': 1, 'y': 1}

#8-10
squares = {i:i*i for i in range(10)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
'''

##### 9장 함수 ######
### 구간 소수 판정 프로그램 함수화###
def is_prime(n) -> bool :
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean type으로 return
    :param n: 판정할 매개변수
    :return: 소수면 True, 아니면 False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n :
            if n % i == 0:
                return False
            i += 1
    return True

# help(is_prime) # 함수에 대한 설명 출력

numbers = input("Input First Second number : ").split()
n1, n2 = int(numbers[0]), int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2 + 1):
    if is_prime(number):
        print(number, end=' ')