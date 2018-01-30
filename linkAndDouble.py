class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


a = Node(1)
b = Node(4)
c = Node(7)
d = Node(9)

a.next = b
b.next = c
c.next = d

b.prev = a
c.prev = b
d.prev = c


print d.prev.value
