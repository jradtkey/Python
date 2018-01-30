class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

def nth_to_last_node(n, node):
    count = 1
    runner = node
    while runner.nextnode:
        count = count + 1
        runner = runner.nextnode
    count = count - n
    runner = node
    i = 0
    while i < count:
        runner = runner.nextnode
        i += 1
    return runner.value

target_node = nth_to_last_node(3, a)

print target_node
