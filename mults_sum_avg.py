# for value in range(1,1001):
#     print value
# for value in range(5,1000001):
#     if value % 5 == 0:
#         print value
a = [1, 2, 5, 10, 255, 3]
total = 0
for value in a:
    total += value
print total
print "average is:", total/len(a)
