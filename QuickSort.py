class Constant:
    def __init__(self):
        self.count = 0
        self.High = "HIGH"
        self.Low = "LOW"
        self.Mid = "MID"

    def reset_count(self):
        self.count = 0


def quickSort(array, Mode):
    """Sort the array by using quicksort."""
    global Con
    pIdx = 0 if Mode == Con.Low else (
        len(array)-1) if Mode == Con.High else (len(array)-1)//2 if Mode == Con.Mid else 0
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[pIdx]
        for x in array:
            if x < pivot:
                Con.count += 1
                less.append(x)
            elif x == pivot:
                Con.count += 1
                equal.append(x)
            elif x > pivot:
                Con.count += 1
                greater.append(x)
        return quickSort(less, Mode)+equal+quickSort(greater, Mode)
    else:
        return array


lst = [1, 51, 2, 4, 32, 5, 6, 22, 7, 5, 7, 23]
Con = Constant()
print(lst)
temp = quickSort(lst[:], Con.High)
print(Con.count, "=>", temp)
Con.reset_count()
temp = quickSort(lst[:], Con.Low)
print(Con.count, "=>", temp)
Con.reset_count()
temp = quickSort(lst[:], Con.Mid)
print(Con.count, "=>", temp)