import itertools

def merge_intervals(input_intervals):
    # input_intervals.sort() ???

    result = []
    low_list = []
    high_list = []

    for i in input_intervals:
        low_list.append(i[0])
        high_list.append(i[1])

    print low_list
    print high_list
    high = high_list[0]
    low = low_list[0]
    for i in range(1,len(low_list)):
        if low_list[i] <= high:
            high = high_list[i]
        if high_list[i] :
            pass
    print high

merge_intervals([[1,4],[3,6],[7,8]])
