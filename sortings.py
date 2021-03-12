def swap(array, i1, i2):
    obj = array[i1]
    array[i1] = array[i2]
    array[i2] = obj


def heapify(array, n, i):
    root = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[root] < array[l]:
        root = l
    if r < n and array[root] < array[r]:
        root = r
    if root != i:
        swap(array, i, root)
        heapify(array, n, root)


def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i = i + 1
            swap(array, i, j)

    swap(array, i + 1, high)
    return i + 1


def countingSort(array, exp):
    output = [0] * len(array)
    count = [0] * 10
    for i in range(0, len(array)):
        index = (array[i] / exp)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len(array) - 1
    while i >= 0:
        index = (array[i] / exp)
        output[count[int(index % 10)] - 1] = array[i]
        count[int(index % 10)] -= 1
        i -= 1
    for i in range(0, len(array)):
        array[i] = output[i]


def selection_sort(array):
    for i in range(0, len(array), 1):
        min = i
        for k in range(i + 1, len(array), 1):
            if array[min] > array[k]:
                min = k
        swap(array, min, i)


def insertion_sort(array):
    if not array:
        return
    for i in range(1, len(array), 1):
        s = array[i]
        j = i - 1
        while j >= 0 and s < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = s


def bubble_sort(array):
    for i in range(0, len(array) - 1, 1):
        b = True
        for k in range(0, len(array) - i - 1, 1):
            if array[k] > array[k + 1]:
                swap(array, k, k + 1)
                b = False
        if b:
            return


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) / 2
        first = array[0:mid]
        second = array[mid:len(array)]
        merge_sort(first)
        merge_sort(second)
        i = j = k = 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                array[k] = first[i]
                i += 1
            else:
                array[k] = second[j]
                j += 1
            k += 1
        while i < len(first):
            array[k] = first[i]
            i += 1
            k += 1

        while j < len(second):
            array[k] = second[j]
            j += 1
            k += 1


def heap_sort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        swap(array, i, 0)
        heapify(array, i, 0)


def quick_sort(array):
    quicksort(array, 0, len(array) - 1)


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


def radix_sort(array):
    max1 = max(array)
    exp = 1
    while max1 / exp > 0:
        countingSort(array, exp)
        exp *= 10


def counting_sort(array):
    finalResult = [0] * len(array)
    count = [0] * 10
    for i in range(0, len(array)):
        count[array[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len(array) - 1
    while i >= 0:
        finalResult[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, len(array)):
        array[i] = finalResult[i]


def bucket_sort(array):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])

    for j in array:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    for i in range(slot_num):
        insertion_sort(arr[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            array[k] = arr[i][j]
            k += 1
    return array


def isSorted(arr):
    if not arr:
        return False
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def testSort(sortFunction):
    testArr0 = None
    testArr1 = []
    testArr2 = [2]
    testArr3 = [2, 6]
    testArr4 = [2, 6, 3, 7, 1, 4, 5]
    testArr5 = [1, 2, 3, 4, 5, 6]
    testArr6 = [6, 5, 4, 3, 2, 1]
    testArr7 = [-2]
    testArr8 = [6, -5, 4, 3, -2, 1]

    cases = [testArr0, testArr1, testArr2, testArr3, testArr4, testArr5, testArr6, testArr7, testArr8]
    for i in cases:
        sortFunction(i)
        print(i, isSorted(i))


if __name__ == '__main__':
    testSort(insertion_sort)