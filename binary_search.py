def binary_search_v1(array: list, x: int):
    """Бинарный (двоичный) поиск. Определяем середину отсортированного списка и сравниваем ее с искомым элементом.
    Если x = середине, то нашли,
    Если x < середины, то ищем в левой половине,
    Если x > середины, то ищем в правой половине."""
    array.sort()
    lowest = 0
    highest = len(array) - 1
    index = None
    while (lowest <= highest) and (index is None):
        mid = (lowest + highest)//2
        if x == array[mid]:
            return mid
        elif x < array[mid]:
            highest = mid - 1
        elif x > array[mid]:
            lowest = mid + 1


def binary_search_v2(array: list, key: int):
    """ Бинарный поиск с определением индексов границ в рамках которых находится число / группа одинаковых чисел"""
    l_left = r_left = -1
    l_right = r_right = len(array)
    while l_right - l_left > 1:
        middle = (l_right + l_left) // 2
        if array[middle] < key:
            l_left = middle
        else:
            l_right = middle
    left = l_left + 1
    while r_right - r_left > 1:
        middle = (r_right + r_left) // 2
        if array[middle] <= key:
            r_left = middle
        else:
            r_right = middle
    right = r_right - 1
    if right < left:
        return 'is missing'
    else:
        return [left, right]


a = [ 1, 2, 3, 4, 6, 7, 8, 9]
print(binary_search_v2(a, 9))