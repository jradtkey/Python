def rev_word(s):
    words = []
    reversedString = " "
    s = s.split()
    print reversedString.join(s[::-1])


    words2 = []
    reversedString2 = ' '
    for j in reversed(s):
        words2.append(j)
    print ' '.join(words2)
rev_word('   Hello John    how are you   ')
