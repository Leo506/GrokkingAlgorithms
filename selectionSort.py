#!/bin/python3

# Алгоритм сортировки выбором
# Выполняется за время O(n)


''' Функция нахождения наименьшего числа в массиве '''
def findSmallest(array):
    smallest = array[0]
    smallestIndex = 0

    for i in range(len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallestIndex = i

    return smallestIndex


''' Функция сортировки выбором  '''
def selectionSort(array):
    newArr = []
    for i in range(len(array)):
        smallest = findSmallest(array)      # Находит наименьший элемент массива
        newArr.append(array.pop(smallest))  # И добавляет его в конец нового массива

    return newArr

print(selectionSort([2, 4, 2, 6, 2, 7, 45, 23]))
