row = []
for num in range(1,13):
    for value in range(1,13):
        row += [value * num]
    print row
    row = []
