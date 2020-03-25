def seqSearch(input, value):
    pos = 0
    found = False
    if pos < size(input) and not found:
         if input[pos] == value:
             found = True
         else:
             pos = pos + 1
     return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
