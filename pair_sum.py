def pairs(arr, k):
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        print target
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num,target)), max(num,target)))

    print output


def pairSum(arr, inti):
    for i in range(len(arr)):
        j = i+1
        while j < len(arr):
            if arr[i] + arr[j] == inti:
                print (arr[i], arr[j])
            j += 1

pairs([1,3,2,2,3], 4)
