def gis(array: list):
    """ Поиск наибольшей общей последовательности чисел в двух массивах """
    f = [0]*(len(array)+1)
    for i in range(1, len(array)+1):
        m = 0
        for j in range(0, i):
            if array[i-1] > array[j-1] and f[j] > m:
                m = f[j]
        f[i] = m + 1
    return max(*f)


# a = [1, 2, 3, 4, 3, 2, 1, 5]
# print(gis(a))


def lcs(a: list, b: list):
    """ Поиск наибольшей возрастающей последовательности чисел в двух массивах"""
    f = [[0]*(len(b)+1) for x in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                f[i][j] = 1 + f[i-1][j-1]
            else:
                f[i][j] = max(f[i-1][j], f[i][j-1])
    return f[-1][-1]


# a = [1, 2, 3, 4, 0, 2, 5]
# b = [1, 2, 3, 0, 1, 5]
# print(lcs(a, b))


def linstein(a: str, b: str):
    """ Поиск редакционного расстояния между строками (Расстояние Ливенштейна) """
    f = [[(i+j) if i*j == 0 else 0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b [j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = 1 + min(f[i-i][j], f[i][j-1], f[i-1][j-1])
    return f[len(a)][len(b)]


a = 'moloko'
b = 'kolokol'
print(linstein(a, b))

