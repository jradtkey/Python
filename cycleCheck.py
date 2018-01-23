class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z
z.next = x

def cycleCheck(node):
    runner1 = node
    runner2 = node.next
    if node.next == None:
        return False
    else:
        while runner2.next.next != None:
            if runner1 == runner2:
                return True
            else:
                runner1 = runner1.next
                runner2 = runner2.next.next
        return False

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z


#############
class TestCycleCheck(object):

    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)

        print "ALL TEST CASES PASSED"

# Run Tests

t = TestCycleCheck()
t.test(cycleCheck)
