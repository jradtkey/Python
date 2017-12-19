def checkType(arg):
    if isinstance(arg, int) and arg >=100:
        print "that's a big number"
    elif isinstance(arg, int) and arg < 100:
        print "that's a little number"
    elif isinstance(arg, str) and len(arg) >= 50:
        print "long sentence"
    elif isinstance(arg, str) and len(arg) < 50:
        print "short sentence"
    elif isinstance(arg, list) and len(arg) >= 10:
        print "big list"
    elif isinstance(arg, list) and len(arg) < 10:
        print "short list"


sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
checkType(eL)
