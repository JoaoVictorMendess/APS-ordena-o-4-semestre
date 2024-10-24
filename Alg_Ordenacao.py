# Função Bubble Sort
def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


# Função Insertion Sort
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# Função Selection Sort
def selection_sort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


# Função Merge Sort
def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1
    return a


# Função Quick Sort
def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[len(a) // 2]
        esq = [x for x in a if x < pivot]
        meio = [x for x in a if x == pivot]
        direita = [x for x in a if x > pivot]
        return quick_sort(esq) + meio + quick_sort(direita)


# Função pra rodar todos ao mesmo tempo
def test_sorting_algorithms():
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Array Original:", arr)
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Insertion Sort:", insertion_sort(arr.copy()))
    print("Selection Sort:", selection_sort(arr.copy()))
    print("Merge Sort:", merge_sort(arr.copy()))
    print("Quick Sort:", quick_sort(arr.copy()))


# Rodar
test_sorting_algorithms()
