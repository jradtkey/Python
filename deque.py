class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.insert(len(self.items), item)

    def removeFront(self):
        front = self.items[0]
        self.items = self.items[1:]
        print front
        return front

    def removeRear(self):
        rear = self.items[len(self.items)-1]
        self.items = self.items[:len(self.items)-1]
        print rear
        return rear

    def isEmpty(self):
        print self.items == []
        return self.items == []

    def size(self):
        print len(self.items)
        return len(self.items)



d = Deque()
d.addFront('hello')
d.addRear('world')
d.size()
print d.removeFront() + ' ' +  d.removeRear()
d.size()
