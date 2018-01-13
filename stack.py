# #LAST IN FIRST OUT
#
# class Stack(object):
#
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         print self.items == []
#         return self.items == []
#
#     def push(self,item):
#         self.items.append(item)
#         print self.items
#
#     def pop(self):
#         print self.items.pop()
#         self.items.pop()
#
#     def peek(self):
#         print self.items[len(self.items)-1]
#         return self.items[len(self.items)-1]
#
#     def size(self):
#         print len(self.items)
#         return len(self.items)
#
#
# s = Stack()
# s.push("hello")
# s.push("world")
# s.pop()

arr = [5,3,0]
print arr
arr.append(4)
print arr
arr.pop()
print arr
