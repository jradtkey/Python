str1 = "clintll eastwood"
str2 = "ollld west action"

def anagram(s1, s2):
    arr1 = []
    arr2 = []

    for j in range(len(s1)):
        if s1[j] != " ":
            arr1.append(s1[j].lower())
    for j in range(len(s2)):
        if s2[j] != " ":
            arr2.append(s2[j].lower())

    if len(arr2) == len(arr1):
        print True
    else:
        print False

anagram(str1, str2)
