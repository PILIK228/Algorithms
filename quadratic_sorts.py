# Quadratic sorts, O(N**2)

def insert_sort(array: list):
    """ Сортировка списка вставками """
    n = len(array)
    for top in range(1,n):
        k = top
        while k > 0 and array[k] < array[k-1]:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1
    return array


def choice_sort(array: list):
    """ Сортировка списка методом выбора """
    n = len(array)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]
    return array


def bubble_sort(array: list):
    """ Сортировка списка методом пузьрков """
    n = len(array)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]
    return array


# array = [2, 4, 3, 5, 6, 4, 3, 1, 6]
# print(insert_sort(array), choice_sort(array), bubble_sort(array), sep='\n')