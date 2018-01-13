class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        # possible:
        #return self.items = self.items[1:]
        return self.items.pop(0)

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
d.isEmpty()
