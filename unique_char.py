def uni_char(s):
    arr = []
    for i in range(len(s)):
        if s[i] in arr:
            print False
            return False
        else:
            arr.append(s[i])
    print True
    return True


uni_char('goo')
