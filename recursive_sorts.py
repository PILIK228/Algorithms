# Recursive sorts

def merge_sort(array: list):
    """ Сортировка массива слиянием. O(N*log2(N) """
    if len(array) <= 1:
        return
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        else: # right[j] > left[i]
            array[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    return array


def quick_sort(array: list):
    """ Быстрая сортировка (Тони Хоара). O(log2(N))"""
    if len(array) <= 1:
        return 1
    barrier = array[0]
    left = []
    middle = []
    right = []
    for x in array:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    quick_sort(left)
    quick_sort(right)
    k = 0
    for x in (left + middle + right):
        array[k] = x
        k += 1
    return array


def check_sorted(array: list, asc=True):
    """ Проверка отсортированности массива за O(N)"""
    flag = True
    s = 2*int(asc) - 1 # asc(True) = 1, desc(False) = 0
    for i in range(0, len(array) - 1):
        if s * array[i+1] < s * array[i]:
            flag = False
            break
    return flag


a = [2, 3, 4, 4, 7, 3, 10, 22, 123, 1]
print(check_sorted(merge_sort(a)))
print(check_sorted(quick_sort(a)))