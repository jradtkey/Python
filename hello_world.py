# new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x = sorted(x)
list1 = x[:len(x)/2]
x = x[(len(x)/2)-1:]
print x
print list1
x[0] = list1
print x

# first and last
'''
y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]
z = y[0] + ' ' + y[len(y)-1]
print z
'''

# min and max
'''
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
'''

# find and replace
'''
words = "It's thanksgiving day. It's my birthday, too!"
def new(word):
    for letter in range(0, len(words)-1):
        check = ""
        if words[letter-1] == " ":
            while words[letter] != " ":
                check += words[letter]
                letter += 1
                if check == "day":
                    return letter-3
            check = ""
idx = new(words)
print idx
import string
new_words = string.replace(words, 'day', 'month')
print new_words
'''
