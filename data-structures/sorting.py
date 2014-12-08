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

data = [77, 11, 5, 2, 34, 3, 2, 99, -1, 8, 1, 11, 25, 0]
print insertionSort(data)
print selectionSort(data)
print bubbleSort(data)
print mergeSort(data)
