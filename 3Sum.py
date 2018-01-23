def threeSum(arr):

    newArr = []
    new = []
    for i in range(len(arr)):
        j = 0
        b = j+1
        if i == j:
            continue
        if i == b:
            continue
        while b < len(arr):
            print arr[i]
            print arr[j]
            print arr[b]
            if arr[i] + arr[j] + arr[b] == 0:
                new.append(arr[i])
                new.append(arr[j])
                new.append(arr[b])
                new.sort()
                if new not in newArr:
                    newArr.append(new)
                new = []
            b = b + 1
    print newArr
arr = [3,0,-2,-1,1,2]
threeSum(arr)
