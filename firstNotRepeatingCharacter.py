def firstNotRepeatingCharacter(s):

    seen = {}
    arr =[]

    for i in range(len(s)):
        if (s[i] not in seen):
            seen[s[i]] = 1
        else:
            seen[s[i]] += 1
    print seen
    for key in seen:
        if seen[key] == 1:
            arr.append(key)

    print arr

    for i in range(len(s)):
        if s[i] in arr:
            print s[i]
            return s[i]

    print "_"
    return "-"

firstNotRepeatingCharacter("abacabaabacaba")
