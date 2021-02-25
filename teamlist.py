
#team list task#
import time
print("Welcome to the EPIC free robux team")
repeat = 1
imperative = 0
command = 0
members = ["darth mander","isaac vader", "sam the mander man", "DOOM"]

while repeat == 1:
     print("1. Start the EPIC")
     command = input("")
     if command == 1:
         print("1. Display full team list")
         print("2. Add New Member to the Team")
         print("3. Delete Member from the team")
         print("4. Quit program")

         imperative = input("")
         if imperative == 4:
             command = 0
         if imperative == 3:
             time.sleep(1)
             print("choose which member to be booted off the team, what a bunch of losers")
             time.sleep(1)
             print(members)
             print("choose based on their number")
             delete = int(input())
             pop





     else:
         print("error")