def ascii_deletion_distance(str1, str2):
    arr = []
    ASCII = {
        'a': 97,
        'b': 98,
        'c': 99,
        'd': 100,
        'e': 101,
        'f': 102,
        'g': 103,
        'h': 104,
        'i': 105,
        'j': 106,
        'k': 107,
        'l': 108,
        'm': 109,
        'n': 110,
        'o': 111,
        'p': 112,
        'q': 113,
        'r': 114,
        's': 115,
        't': 116,
        'u': 117,
        'v': 118,
        'w': 119,
        'x': 120,
        'y': 121,
        'z': 122
    }
    num = 0

    # if len(str1) > len(str2):
    for value in range(len(str1)):
        if str1[value] not in str2:
            arr.append(str1[value])

    # else:
    for value in range(len(str2)):
        if str2[value] not in str1:
            arr.append(str2[value])


    for i in arr:
        num += ASCII[i]

    print arr
    return num

ascii_deletion_distance("thought", "sloughs")
