def f(n: int):
    """ Вычисление факториала натурального числа """
    assert n >= 0
    if n == 0:
        return 1
    return f(n-1) * n

def gcd(a, b):
    """ АЛГОРИТМ ЕВКЛИДА - Поиск наибольшего общего делителя чисел a и b, где a > b """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def pow(a: float, n: int):
    """ Быстрое возведение числа в степень """
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n-1) * a
    else:
        return pow(a**2, n//2)


# print(f(5))
# print(gcd(45, 25))
# print(pow(6, 7))


