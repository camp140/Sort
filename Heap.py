from math import log2
from math import floor


def print90(h, i, max_i):
    if i <= max_i:
        indent = floor(log2(i+1))
        print90(h, (i*2)+2, max_i)
        print('     ' * indent, h[i])
        print90(h, (i*2)+1, max_i)


def insertMinHeap(h, i):
    print('insert', h[i], 'at index ', i, end=' ')
    print(h)
    insertEle = h[i]
    fi = (i-1)//2
    while i > 0 and insertEle < h[fi]:
        h[i] = h[fi]
        i = fi
        fi = (i-1)//2
    h[i] = insertEle


def deleteMin(h, last):
    print('delMin', h[0], 'last index = ', last, end='     ')
    print(h)
    insertEle = h[last]
    h[last] = h[0]
    hole = 0
    ls = hole*2 + 1
    found = False
    while ls < last and not found:
        rs = ls if ls+1 >= last else ls+1
        min = ls if h[ls] < h[rs] else rs  # minson index
        if h[min] < insertEle:
            h[hole] = h[min]  # promote small son up to hole
            hole = min  # going down the tree
            ls = hole*2+1
        else:
            found = True
    h[hole] = insertEle


h = [213, 13, 14, 21, 19, 16, 65, 24, 68, 26, 32, 12, 123, 213, 213, 213]
temp = []
for i in range(0, len(h)):
    temp.append(h[i])
    insertMinHeap(h, i)
    print(h)
    print90(h, 0, i)
    print("----------------------------------\n")

sortArr = []
for last in range(len(h)-1, -1, -1):
    sortArr.append(h[0])
    deleteMin(h, last)
    print(h)
    print90(h, 0, last)
    print('------------------\n')

print("===========sorting a ============")
print(temp)
print(sortArr)
print()