def finder(arr1,arr2):
    dict1 = {}
    dict2 = {}

    for i in range(len(arr1)):
        if arr1[i] in dict1:
            dict1[arr1[i]] += 1
        else:
            dict1[arr1[i]] = 1

    for i in range(len(arr2)):
        if arr2[i] in dict2:
            dict2[arr2[i]] += 1
        else:
            dict2[arr2[i]] = 1

    for key in dict1:
        if key not in dict2:
            print key
            return key
        else:
            dict1[key] -= dict2[key]

    for key in dict1:
        if dict1[key] > 0:
            print key
            return key



arr1 = [9,8,7,6,5,4,3,2,1]
arr2 = [9,8,7,5,4,3,2,1]
finder(arr1,arr2)
