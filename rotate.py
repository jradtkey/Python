def rotateImage(a):

    b = []
    j = 0

    a = a[::-1]
    arr = []
    print a
    for i in range(len(a)):
        print "i =", i
        while j < len(a):
            arr.append(a[j][i])
            j = j+1
        b.insert(i, arr)
        arr = []
        j = 0
    print b



a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

rotateImage(a)

# rotateImage(a) =
#     [[7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3]]
