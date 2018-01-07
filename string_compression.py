def compress(s):
    dic = {}
    count = 0
    arr = []
    for j in range(len(s)):
        if s[j] in dic:
            dic[s[j]] += 1
        else:
            dic[s[j]] = 1
    for key in dic:
        arr.append(key)
        arr.append(str(dic[key]))
    print "".join(arr)

compress('AAHHBBYYyytTT')
