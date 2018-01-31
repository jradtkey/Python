def balance_check(bracket_string):

    arr1 = []
    arr2 = []
    arr3 = []

    if len(bracket_string)%2 != 0:
        print False
        return False

    for i in range(len(bracket_string)):
        if bracket_string[i] == "(":
            arr1.append(bracket_string[i])
        elif bracket_string[i] == ")":
            if len(arr1) == 0:
                print False
                return False
            else:
                arr1.pop()


    print len(arr1)

balance_check('((())')
