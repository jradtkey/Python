def balance_check(s):

    arr1 = []
    arr2 = []
    arr3 = []

    for i in range(len(s)):
        if s[i] == "(":
            arr1.append(s[i])
        elif s[i] == ")":
            if len(arr1) == 0:
                print False
                return False
            else:
                arr1.pop()
        elif s[i] == "[":
            arr2.append(s[i])
        elif s[i] == "]":
            if len(arr2) == 0:
                print False
                return False
            else:
                arr2.pop()
        elif s[i] == "{":
            arr3.append(s[i])
        elif s[i] == "}":
            if len(arr3) == 0:
                print False
                return False
            else:
                arr3.pop()
    print arr1
    print arr2
    print arr3


    if len(arr1) > 0 or len(arr2) > 0 or len(arr3) > 0:
        print False
        return False
    else:
        print True
        return True

balance_check('[](){([[[]]])}(')
