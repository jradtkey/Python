class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

def reverse(head):
    prev = None
    current = head
    nextnode = None
    while current:
        nextnode = current.nextnode
        current.nextnode = prev
        prev = current
        current = nextnode

    return prev


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print a.nextnode.value
print b.nextnode.value
print c.nextnode.value



reverse(a)

print d.nextnode.value
print c.nextnode.value
print b.nextnode.value
