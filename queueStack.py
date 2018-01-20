class Queue2Stacks(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()

q = Queue2Stacks()

for i in xrange(5):
    q.enqueue(i)

for i in xrange(5):
    print q.dequeue()
