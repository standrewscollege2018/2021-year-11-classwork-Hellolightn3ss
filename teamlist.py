
#team list task#
import time
print("Welcome to the EPIC free robux team")
repeat = 1
imperative = 0
command = 0
number = 0
#this is setting the variable back to 0, in order to reset the program
members = ["darth mander","isaac vader", "sam the mander man", "DOOM", "tsundere", "BAKA", "enduser","your average kirito wanna be isekai protagonist"]
# setting up the team member list, and saying that while repeat = 1 the program will run forever
while repeat == 1:
     print("1. Start the EPIC")
     command =input("")
     #if the input for start the epic is 1 then the program will continue, if not it will not
     if command=="1":
         if imperative == 0:
            print("1. Display full team list")
            print("2. Add New Member to the Team")
            print("3. Delete Member from the team")
            print("4. Quit program")
            number = input("")
            time.sleep(1)
            #this is the display which shows the 4 options
            if number == "4":
                command = 0
                #sets the command back to 0, bringing the program back to the start
            if number == "3":
                time.sleep(1)
                print("choose which member to be booted off the team, what a bunch of losers")
                time.sleep(1)
                print(members)
                print("choose based on their number")
                delete = int(input())
                members.pop(delete-1)
                imperative = 0
                command = 1
                number = 0
                #this shows the list of members then using the integer number of the place the team member is then kicks them off
            if number == "2":
                print("imput the name of the new member")
                new=input("")
                time.sleep(1)
                members.append(new)
                imperative = 0
                number = 0
                command = 1
                #basicaling input it, then adds it
            if number =="1":
                print(members)
                time.sleep(5)
                print("do you wish to go back, if yes do Y")
                leave=input("")
                if leave == "Y":
                    number = 0
                    imperative = 0
                    command = 1
                    # if choose Y then it goes back to the screen
else:
    print("error")