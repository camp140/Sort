def selectionSort(list):
    compare = 0
    swap = 0
    for last in range(len(list)-1, 0, -1):
        biggest = 0
        for i in range(last):
            if list[i] > list[biggest]:
                biggest = i
            compare += 1
        list[last], list[biggest] = list[biggest], list[last]
        swap += 1
    print(f'compare: {compare}')
    print(f'swapped: {swap}')

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list = [2, 5, 9, 3, 4, 8, 7, 6, 1]
selectionSort(list)
print(list)
