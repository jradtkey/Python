import random
def coins(arg):
    heads = 0
    tails = 0
    for value in range(1,arg):
        x = random.random()
        print round(x)
        if round(x) == 0.0:
            heads += 1
            print "Attempt #" + str(value) + ": Throwing a coin...It's a head!...Got", str(heads), "heads so far and", str(tails), "tails so far"
        elif round(x) == 1.0:
            tails += 1
            print "Attempt #" + str(value) + ": Throwing a coin...It's a tail!...Got", str(heads), "heads so far and", str(tails), "tails so far"
coins(501)
