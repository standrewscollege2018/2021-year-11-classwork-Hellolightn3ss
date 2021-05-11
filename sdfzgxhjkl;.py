#this is a quiz, made by Daniel Robertson
#imports the Time and Random aspects of the code so that it's usable
import time
import random
'''
these lists contain the questions that will be used under the list name Questions
as well as the answers under the list "answers", and other choices that can be made, as the quiz is multi choice
under the list names "multi_choice_1" and "multi_choice_2"
There are also strings of text that will be printed after text, this is under the lists "compliments" and "insults"
'''
questions=["which type of hair colour guarantees that they aren't going to be together with the protagonist","who lives in a pineapple under the sea","when the world needed him most who disappeared?","no one expects the","In Japan the Aonami line, in Nagoya has been in to what?","hello there is responded with","your bad lol is said by who"]
answers=["blue","spongebob squarepants","the avatar","french inquisition","the ayanami line","general kenobi","said by Gabith"]
multi_choice_1=["pink","Patrick star","Bernny sanders","french revelution","the Rei 2 line","darth kermit","Said by Sam smith"]
multi_choice_2=["green","my mother","obama's last name","the british royal family","the blue line","Kermit","Said by Isaac mander"]
compliments=["Correct, well done maybe your aren't an idiot after all","Correct, not bad, not great, onto the next one","Correct, mission complete, respect+","Correct, you might just have enough worth to be raised as cattle.","Correct, make way, make way, primitive man coming through","Correct, nearing the end, if you get the next one right, I MIGHT acknowledge you as a fellow human","Correct, well done, it not like I am proud or anything *tsun intensifies*"]
insults=["Incorrect, are you sure you have more than 1 brain cell?","Incorrect, are you sure you don't need to get your brain checked","Incorrect, a jellyfish has greater intellect than you","Incorrect, if I were to jump from a dog's IQ to your's I would die on impact from the fall","Incorrect, you moronic imbecile of a monkey","Incorrect, guess you can't teach a dumb man new tricks","Incorrect, so close, yet so far"]
question_number=0
sleep = 1
random_interger=0
userscore = 0
error = 0
keep_asking= True
#defining the variables used in the program, at the start of the program
print("please input the user's name")
print("input here")
name=input("")
#asking for the user's name, and then setting variable "name" to the input
time.sleep(sleep*2)
print("welcome",name,"this quiz will have 7 questions, and these will determind the value of your life")
time.sleep(sleep*3)
print("how many questions do you believe you will answer correctly?")
time.sleep(sleep*2)
print("if you type anything that isn't your intented answer or a legitament answer it will be taken as your answer")
time.sleep(sleep*2)
#printing out the intructions for the quiz so that the user knows what to do, with time.sleep commands to ensure it;s easier to read
#After asking for a guess of how questions they will get correct, setting "guess" to the user input.while keep_asking == True:
while keep_asking == True:
    try:
        guess = int(input("how many questions do you think you will get right?"))
        if guess <0 or guess > len(questions):

            print ("invalid amount of questions")
        else:
            keep_asking = False
            print("time to start losers")
            for space in range (0,3):
            print()
    except:
        print("enter an interger please")

for question_number in range (0,7):
#repeats 7 times, until question_number is 7
    random_interger=random.randint(1,3)
    #sets random_interger to a randon interger between 1 and 3
    if random_interger == 1:
    #if  random_interger was set to 1, it prints the question, then answer, multi_choice_1 and then multi_choice_2
    #in that orderd, each have 1. or 2. or 3. in front of them, and then setting "useranswer" to the input from the user.
        print(questions[question_number])
        print("1.",answers[question_number])
        print("2.",multi_choice_1[question_number])
        print("3.",multi_choice_2[question_number])
        useranswer=input("")
    elif random_interger == 2:
        print(questions[question_number])
        print("1.",multi_choice_1[question_number])
        print("2.",answers[question_number])
        print("3.",multi_choice_2[question_number])
        useranswer=input("")
    #if  random_interger was set to 2, it prints the question, then multi_choice_1, answer and then multi_choice_2
    #in that orderd, each have 1. or 2. or 3. in front of them, and then setting "useranswer" to the input from the user.
    else:
        print(questions[question_number])
        print("1.",multi_choice_2[question_number])
        print("2.",multi_choice_1[question_number])
        print("3.",answers[question_number])
        useranswer=input("")
    #if  random_interger was set to 1, it prints the question, then multi_choice_2, multi_choice_1 and then answer
    #in that orderd, each have 1. or 2. or 3. in front of them, and then setting "useranswer" to the input from the user.
    if useranswer == answers[question_number] or random_interger:
    #if the answer that the user types in is the correct word or number then it prints that it's correct
    #then a compliment, makes spaces, so that the next question will be easier to read and then increases "userscore"
        time.sleep(0.75*sleep)
        print(compliments[question_number])
        time.sleep(1.5*sleep)
        for space in range (0,3):
            print()
        userscore=userscore+1
    else :
    #if the answer that the user types in isn't the correct word or number then it prints that it's incorrect
    #then an insult, makes spaces, so that the next question will be easier to read and then procends to the next question
        time.sleep(0.75*sleep)
        print(insults[question_number])
        time.sleep(1.5*sleep)
        for space in range (0,3):
            print()
#prints the ending code like how well the user did, and how it compares to the guess they made at the start of the quiz
print("now that we have reach the end of the worth evaluation quiz lets see how you did")
time.sleep(3*sleep)
print(guess,"this is how you assumed or maybe wished you did")
time.sleep(3*sleep)
print("and this is how you did",userscore)