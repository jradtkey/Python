def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

A1 = range(10)
# [0,1,2,3,4,5,6,7,8,9]

A2 = sorted([i for i in A1 if i in A0])
# []

A3 = sorted([A0[s] for s in A0])
# [1,2,3,4,5]

A4 = [i for i in A1 if i in A3]
# [1,2,3,4,5]

A5 = {i:i*i for i in A1}
# {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}

A6 = [[i,i*i] for i in A1]
# [[0,0], [1,1], [2,4], [3,9], [4,16], [5,25], [6,36], [7,49], [8,64], [9,81]]


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
# [0,1]

f(3,[3,2,1])
# [3,2,1,0,1,4]

f(3)
# [0,1,0,1,4]
