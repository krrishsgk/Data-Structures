class Node:
    def __init__(self, inititem):
        self.data = inititem
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def addData(newitem):
        self.data = newitem

    def setNext(address):
        self.next = address

class unorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addElement(self, element):
        temp = Node(element)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    
