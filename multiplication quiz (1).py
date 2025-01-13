#Scarlett 
#1/9
#Multiplication Quiz

#Init
import random
import time
score = 0
#Functions
def multquiz():
    print("Welcome to the Multiplication Quiz!")
    print("How Many Questions Would You Like to Answer?")
    questions = input("How Many Questions Would You Like to Answer?") #String
    start_time = time.time()
    for i in range(int(questions)):
        global score
        num1 = random.randint(0,10) #Integer
        num2 = random.randint(0,10) #Integer
        answer = num1 * num2
        print("What is " + str(num1) + "*" + str(num2) + "?") #String
        youranswer = input("What is your answer?") #String
        print("Your answer is: " + str(youranswer)) #String
        if answer == int(youranswer): #Integer
            print("Correct!")
            score = score + 1 #Integer
        else:
            print("Incorrect!")
    end_time=time.time()
    elapsed_time=end_time-start_time
    print("It took you " + str(elapsed_time) + " seconds to complete the quiz.") #String
    print("Your Final Score Is: " + str(score) + "/" + str(questions) + "!") #String
#Main
multquiz()

