import random
def grade():
    print "Scores and Grades"
    for i in range(0,6):
        score = random.randint(60, 100)
        if score > 59 and score < 70:
            print "Score:", str(score) + "; Your grade is D"
        elif score > 69 and score < 80:
            print "Score:", str(score) + "; Your grade is C"
        elif score > 79 and score < 90:
            print "Score:", str(score) + "; Your grade is B"
        elif score > 89:
            print "Score:", str(score) + "; Your grade is A"
    print "End of program. Bye!"
grade()
