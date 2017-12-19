def findCharacters(arg, char):
    new_list = []
    for value in word_list:
        if char in value:
            new_list.append(value)
    print new_list

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
findCharacters(word_list, char)
