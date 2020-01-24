class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(names, position):
    order = Queue()
    for name in names:
        order.enqueue(name)
    i = 1
    while order.size() > 1:
        if i % (position+1) == 0:
            order.dequeue()
        else:
            order.enqueue(order.dequeue())
        i = i + 1

    return order.dequeue()

def main():
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

main()
