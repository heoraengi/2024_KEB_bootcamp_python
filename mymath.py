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


def fahrenheit_to_celsius(fahrenheit) -> float:
    return  ((fahrenheit - 32.0) * 5.0 / 9.0)