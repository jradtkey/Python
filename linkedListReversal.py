class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head):
    current = head
    prev = None
    nextnode = None
    while current:
        nextnode = current.next
        current.next = prev
        previous = current
        current = nextnode
    print previous

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

print a.next.value
print b.next.value
print c.next.value



reverse(a)

print d.next.value
print c.next.value
print b.next.value
