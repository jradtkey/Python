def categorize(temp):

    if temp <=32:
        print "Freezing"
    elif temp > 32 and temp < 55:
        print "Cold"
    elif temp >= 55 and temp < 75:
        print "Mild"
    elif temp >= 75 and temp < 95:
        print "Hot"
    elif temp >= 95:
        print "Scorching"




categorize(95)
