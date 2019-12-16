def shellSort(list):
    n = len(list)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = list[i]
            j = i
            while j >= gap and list[j-gap] > temp:
                list[j] = list[j-gap]
                j -= gap
            list[j] = temp
        gap //= 2

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list = [2, 5, 9, 3, 4, 8, 7, 6, 1]
shellSort(list)
print(list)