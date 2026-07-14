'''
#факториал рекурсия
def factorial(n : int) -> int:
    if n ==0:
        return 1

    return n * factorial(n-1)

print(factorial(996))
'''

'''
#подсчет сумма
def sum(x : int) -> int:
    if x == 0:
        return 0
    return x + sum(x-1)

print(sum(113))

'''
'''
#подсчет сумма элементов списка
def sum(x : list) -> int:

    if len(x) == 0:
        return 0
    return x[0] + sum(x[1:])

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
'''

def quicksort(arr : list) -> list:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 7, 8, 9, 1, 5]))


