def binary_search(array: list, x: int):
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
            