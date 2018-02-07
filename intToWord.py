#5 - five
#15 - fifteen
#52 - fifty two
#571 - five hundred seventy one
#5819 - five thousand eight hundred nineteen
#5698 - fifty six thousand six thousand ninety eight



def toWord(num):
    words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'fourty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety'
    }

    num = str(num)
    output = ''
    length = len(num)

    for i in range(length):
        if len(num) == 1:
            output = output + ' ' + words[num]
            print output
            break
            # print words[num]
        elif len(num) == 2:
            if num[1] == '0':
                output = output + ' ' + words[num]
                print output
                break
            else:
                if int(num) < 20:
                    output = output + ' ' + words[num[0]+num[1]]
                    print output
                    break
                output = output + ' ' + words[num[0]+'0']
                num = num[1:]

        elif len(num) == 3:
            if num[1] == '0' and num[2] == '0':
                output += words[num[0]] + ' ' + 'hundred'
                print output
                return output
            else:
                print 'not whole'
                output = output + ' ' +words[num[0]] + ' ' + 'hundred'
                print output
                num = num[1:]
                print num
        elif len(num) == 4:
            if num[1] == '0' and num[2] == '0' and num[3] == '0':
                output += words[num[0]] + ' ' + 'thousand'
                print output
                return output
            else:
                output = output + ' ' + words[num[0]] + ' ' + 'thousand'
                num = num[1:]
        elif len(num) == 5:
            if num[1] == '0' and num[2] == '0' and num[3] == '0' and num[4] == '0':
                output += words[num[0]+'0'] + ' ' + 'thousand'
                print output
                break
            else:
                output = output + ' ' + words[num[i]+'0']+ ' ' + words[num[1]] + ' ' + 'thousand'
                print output
                num = num[2:]
toWord(90000)
