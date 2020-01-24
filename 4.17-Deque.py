class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)


def checkPalindrome(string):
    storage = Deque()

    for letter in string:
        storage.addRear(letter)

    balanced = True
    while storage.size() > 1:
        front = storage.removeFront()
        back = storage.removeRear()
        if front == back:
            balanced = True
        else:
            balanced = False
            break

    return balanced

def main():
    print(checkPalindrome("madam"))
    print(checkPalindrome("blue"))
    print(checkPalindrome("malayalam"))
    print(checkPalindrome("gopalakrishnan"))

main()
