import math
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
