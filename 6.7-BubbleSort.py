def bubbleSort(alist):
    counter = 0
    while counter <= len(alist)-1:
        for i in range(counter, len(alist)-1):
            if alist[i] < alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        counter = counter + 1

    return alist


testlist = [54,26,93,17,77,31,44,55,20]
bubbleSort(testlist)
print(testlist)
