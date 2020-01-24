from pythonds.basic import Stack

def Dec2Bin(dec, base):
    digits = "0123456789ABCDEFGHIJKLMNOP"
    container = Stack()
    while dec > 0:
        remainder = dec % base
        container.push(remainder)
        dec = dec // base
    binstring = ""
    while not container.isEmpty():
        binstring = binstring + str(digits[container.pop()])

    return binstring

def main():
    print(Dec2Bin(26, 26))

main()
