
#team list task#
import time
print("Welcome to the EPIC free robux team")
repeat = 1
imperative = 0
command = 0
number = 0
members = ["darth mander","isaac vader", "sam the mander man", "DOOM"]

while repeat == 1:
     print("1. Start the EPIC")
     command = input("")
     if command=="start":
         if imperative == 0:
            print("1. Display full team list")
            print("2. Add New Member to the Team")
            print("3. Delete Member from the team")
            print("4. Quit program")

             number = input("")
             time.sleep(1)
             print("baka")
            if number == 4:
                command = 0
            if number == 3:
                time.sleep(1)
                print("choose which member to be booted off the team, what a bunch of losers")
                time.sleep(1)
                print(members)
                print("choose based on their number")
                delete = int(input())
                members.pop(delete)
                imperative = 0
            if number == 2:
                print("imput the name of the new member")
                new=input("")
                time.sleep(1)
                members.append(new)
                imperative = 1
            if number ==1:
                print(members)
                time.sleep(5)
                print("do you wish to go back, if yes do Y if no do N")
                leave=input("")
                if leave == Y:
                    imperative=0
                if leave == N:
                    imperative=1

     else:
         print("error")