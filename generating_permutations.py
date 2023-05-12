# Генерация всех перестановок
def generate_numbers(n: int, m: int, prefix=None):
    """ Генерирует все числа (с лидирующими незначимыми нулями) в n-"ричной" системе исчисления (n <= 10) длины m """
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m-1, prefix)
        prefix.pop()


def gen_bin(m: int, prefix=None):
    """ Генерирует все числа (с лидирующими незначимыми нулями) в двоичной системе исчисления длины m """
    if m == 0:
        print(prefix)
        return
    else:
        generate_numbers(m-1, prefix+"0")
        generate_numbers(m-1, prefix+"1")


def find(number, a):
    """ Ищет number в 'а' и возвращает True / False """
    for i in a:
        if i == number:
            return True
    return False


def generate_permutations(n: int, m: int =-1, prefix=None):
    """ Генерация перестановок n чисел в m позоциях с префиксом prefix"""
    if m == -1:
        m = n
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for number in range(1, n+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(n, m-1, prefix)
        prefix.pop()


# print('generate_numbers: ')
# print(generate_numbers(2, 3))
# print('generate_permutations: ')
# print(generate_permutations(3, 3))


