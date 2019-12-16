def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
                list[j + 1] = list[j] 
                j -= 1
        list[j + 1] = key 

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list = [2, 5, 9, 3, 4, 8, 7, 6, 1]
insertionSort(list)
print(list)