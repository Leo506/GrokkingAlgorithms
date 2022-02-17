#!/bin/python3

# Алгоритм быстрой сортировки
# Выполняется за время O(n*log n)

def quicksort(array):
    if len(array) < 2:
        return array  # Базовый случай: массивы с 0 и 1 элементом уже "отсортированы"
    else:
        # Рекурсивный случай
        pivotIndex = int(len(array) / 2)
        pivot = array[pivotIndex]  # Выбираем опорный элемент

        less = [i for i in array[:pivotIndex] if i <= pivot] + [i for i in array[pivotIndex+1:] if i <= pivot]

        greater = [i for i in array[:pivotIndex] if i > pivot] + [i for i in array[pivotIndex+1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 4, 4, 4, 23, 34, 23, 34, 54, 232, 23, 345, 232]))
