def rec_sum(n):

    # base case
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)


def sum_func(n):

    first = str(n)
    if str(n%10) == first[0]:
        return n
    else:
        return n%10 + sum_func(n/10)


def word_split(phrase, list_of_words, output = None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output

print word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
