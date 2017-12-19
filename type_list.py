def checkType(arr):
    newString = ""
    newInt = 0
    for value in arr:
        if isinstance(value, str):
            newString += " " + value
        elif isinstance(value, int) or isinstance(value, float):
            newInt += value
    if len(newString) > 0 and newInt != 0:
        print "The list you entered is of mixed type"
        print "String:",newString
        print "Sum:", str(newInt)
    elif len(newString) > 0 and newInt == 0:
        print "The list you entered is of string type"
        print "String:", newString
    elif len(newString) == 0 and newInt != 0:
        print "The list you entered is of integer type"
        print "Sum:", str(newInt)

l = [2,3,1,7,4,12]

checkType(l)
