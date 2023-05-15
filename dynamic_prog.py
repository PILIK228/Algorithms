# Dynamic programming

def fib(n: int):
    """ Поиск числа Фиббоначе за O(N) """
    fib_array = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib_array[i] = fib_array[i-1] + fib_array[i-2]
    return fib_array[n]


# print(fib(6))


