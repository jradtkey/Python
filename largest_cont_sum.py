def large_cont_sum(arr):
    largestSum = arr[0]
    currentSum = arr[0]

    for i in range(1, len(arr)):
        currentSum += arr[i]
        print currentSum
        print largestSum
        if currentSum > largestSum:
            largestSum = currentSum
    print "Largest Sum:", largestSum

large_cont_sum([1,2,-1,3,4,-1])
