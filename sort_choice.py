def sort_choice(array: list):
    """ Сортировка выборкой, делим список на две части (отсортированная и не отсортированная).
    Проходим по правой части, сравнивая ее с элементами левой. """
    for i in range(len(array)):
        lowest = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest]:
                lowest = j
            array[i], array[lowest] = array[lowest], array[i]
    return array

