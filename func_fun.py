def odd_even():
    for value in range(1,2001):
        name = str(value)
        if value % 2 == 0:
            print "Number is ", name, ". This is an even number"
        elif value % 2 != 0:
            print "Number is", name, ". This is an odd number"
#odd_even()

def multiply(arr, multiple):
    new_arr = []
    for value in arr:
        new_arr += [value * multiple]
    return new_arr
arg = [2,4,5]
multiple = 3


def layered(param):
    idx = []
    another = []
    for value in param:
        for length in range(0,value):
            idx.insert(length, 1)
        another.append(idx)
    return another
x = layered(multiply(arg, multiple))
print x
