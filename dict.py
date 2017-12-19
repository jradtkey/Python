newDictionary = {
    'name': "Anna",
    'age': 101,
    'country': "USA",
    'language': "Python"
}

def printDict(diction):
    for key in diction:
        print key
        print diction[key]

printDict(newDictionary)
