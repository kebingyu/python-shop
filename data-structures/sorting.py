def insertionSort(data):#{{{
    length = len(data)
    if length >= 2:
        for idx_i in range(1, length):
            tmp = data[idx_i]
            for idx_j in range(idx_i, 0, -1):
                if data[idx_j - 1] > tmp:
                    data[idx_j] = data[idx_j - 1]
                    idx_j = idx_j - 1
                else:
                    break
            data[idx_j] = tmp
    return data
#}}}

def selectionSort(data):#{{{
    length = len(data)
    if length >= 2:
        for idx_i in range(0, length - 1):
            smallest = idx_i
            for idx_j in range(idx_i + 1, length):
                if data[idx_j] < data[smallest]:
                    smallest = idx_j
            if idx_i != smallest:
                data[idx_i], data[smallest] = data[smallest], data[idx_i]
    return data
#}}}

def bubbleSort(data):#{{{
    length = len(data)
    if length >= 2:
        for idx_i in range(0, length - 1):
            idx_j = length - 1
            while idx_j > idx_i:
                if data[idx_j - 1] > data[idx_j]:
                    data[idx_j - 1], data[idx_j] = data[idx_j], data[idx_j - 1]
                idx_j = idx_j - 1
    return data
#}}}

def mergeSort(data):#{{{
    length = len(data)
    if length >= 2:
        mid = length / 2
        data1 = mergeSort(data[:mid])
        data2 = mergeSort(data[mid:])
        data = merge(data1, data2)
    return data

def merge(data1, data2):
    data = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(data1) and idx2 < len(data2):
        if data1[idx1] < data2[idx2]:
            data.append(data1[idx1])
            idx1 = idx1 + 1
        else:
            data.append(data2[idx2])
            idx2 = idx2 + 1
    while idx1 < len(data1):
        data.append(data1[idx1])
        idx1 = idx1 + 1
    while idx2 < len(data2):
        data.append(data2[idx2])
        idx2 = idx2 + 1
    return data
#}}}

def quickSort(data):#{{{
    length = len(data)
    if length > 1:
        largest = 0
        # find the largest and move it to the rightmost
        for _ in range(1, length):
            if data[_] > data[largest]:
                largest = _
        data[largest], data[length - 1] =\
                data[length - 1], data[largest]
        # sort
        quick_sort(data, 0, length - 2)
    return data

def quick_sort(data, fr, to):
    data[fr], data[(fr + to) / 2] =\
            data[(fr + to) / 2], data[fr]
    lower = fr + 1
    upper = to
    pivot = data[fr]
    # partition
    while lower <= upper:
        while data[lower] < pivot:
            lower += 1
        while data[upper] > pivot:
            upper -= 1
        if lower < upper:
            data[lower], data[upper] = \
                    data[upper], data[lower]
        else:
            lower += 1
    data[fr], data[upper] = \
            data[upper], data[fr]
    # search sub array
    if fr < upper - 1:
        quick_sort(data, fr, upper - 1)
    if upper + 1 < to:
        quick_sort(data, upper + 1, to)
#}}}

data = [77, 11, 5, 2, 34, 3, 2, 99, -1, 8, 1, 11, 25, 0]
print insertionSort(data)
print selectionSort(data)
print bubbleSort(data)
print mergeSort(data)
print quickSort(data)
