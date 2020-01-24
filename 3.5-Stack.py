class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)




def parChecker(symbols):
    container = Stack()
    balanced = True
    index = 0
    while index < len(symbols) and balanced:
        if symbols[index] in '({[':
            container.push(symbols[index])
        else:
            if container.isEmpty():
                balanced = False
            elif symbols[index] in ')}]':
                check = container.pop()
                if not matches(check, symbols[index]):
                    balanced = False

        index = index + 1
    if balanced and container.isEmpty():
        return True
    else:
        return False

def matches(opening, closing):
    openers = "([{"
    closers = ")]}"
    return openers.index(opening) == closers.index(closing)


def main():
    parans = "[]{}()"
    print(parChecker(parans))

main()
