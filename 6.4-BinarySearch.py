def binarySearch(alist, item):
    found = False
    first = 0
    last = len(alist) - 1

    while not found and last >= first:
        middle_index = (last + first//2)
        if alist[middle_index] == item:
            found = True
        else:
            if alist[middle_index] > item:
                last = middle_index - 1
            else:
                first = middle_index + 1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
