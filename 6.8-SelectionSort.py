def selectionSort(alist):

    swapPosition = len(alist)-1
    while swapPosition > 0:
        largestItem = 0
        for element in range(swapPosition, 0, -1):
            if alist[element] > alist[largestItem]:
                largestItem = element


        temp = alist[swapPosition]
        alist[swapPosition] = alist[largestItem]
        alist[largestItem] = temp
        swapPosition = swapPosition - 1

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
