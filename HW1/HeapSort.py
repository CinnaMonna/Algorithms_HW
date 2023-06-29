from random import randint


def heapify(arr, n, i):
    '''
    Функция для построения восходящей двоичной кучи
    
    аргументы:
    arr - массив
    n - размер кучи
    i - индекс массива - корень дерева или поддерева

    переменные:
    l - индекс массива - левый дочерний узел
    r - индекс массива - правый дочерний узел
    largest - индекс наибольшего элемента в поддереве
    '''

    largest = i 
    l = 2 * i + 1  
    r = 2 * i + 2   

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    '''
    Функция для сортировки массива

    аргументы:
    arr - массив

    переменные:
    n - размер массива
    '''

    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)


arr = [randint(0, 100) for i in range(10)]
print ("Initial array:\n", arr)
heapSort(arr)
print ("Sorted array:\n", arr)