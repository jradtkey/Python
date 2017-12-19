def compare(list1, list2):
    count = 0
    for value in range(0, len(list1)):
        if list1[value] == list2[value]:
            count += 1
    if count == len(list1):
        print "The lists are the same"
    elif count != len(list1):
        print "The lists are not the same"


list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']
compare(list_one, list_two)
