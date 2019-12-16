def bubbleSort(list):
    count = 0
    compare = 0
    for last in range(len(list) - 1, 0, -1):
        swapped = False
        for i in range(last):
            if list[i + 1] < list[i]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
                count += 1
            compare += 1
        if not swapped:
            break
    print(f"swapped: {count}")
    print(f"compared: {compare}")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list = [2, 1, 3, 5, 4]
bubbleSort(list)
print(list)
