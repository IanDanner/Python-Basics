#Assignment: Scores and Grades
import random
def genScore(num):
    print "Scores and Grades"
    for idx in range(0,num):
        score = random.randint(60,100)
        if score >= 60 and score <= 69:
            print "Score: "+str(score)+"; Your grade is D"
        if score >= 70 and score <= 79:
            print "Score: "+str(score)+"; Your grade is C"
        if score >= 80 and score <= 89:
            print "Score: "+str(score)+"; Your grade is B"
        if score >= 90 and score <= 100:
            print "Score: "+str(score)+"; Your grade is A"
    print "End of the program. Bye!"
genScore(10)