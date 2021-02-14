
print("hello, and welcome to SAOistrash 2021, the ultimate fortnite dance battle driving battle royale POG CHAMP tournament")

print("enter the name of the team competing.")
Mainteam = input("input here")
X=0
badteam = []
win = 0
true =0
repeat = 0
score = 0
while repeat == 0:
    sidecharacter = input("enter the other teams competing")
    if sidecharacter == "done":
         repeat = 1
    while win is true:

        teamnumber = (len(badteam))
        print ("match",Mainteam,"against",badteam[X])
        print ("input the scores of the teams")

        if X == (len(badteam)):
            win = 1
            print("in this tornament", Mainteam,"has obtained",score,"points")
        else:
            Team1score = input(int("enter the interger score for",Mainteam,))
            Team2score = input(int("enter the interger score for",badteam[X],))
        if Team1score > Team2score:
            print(Mainteam,"wins with a score of",Team1score,"against",badteam[X],"of",Team2score,)
            X = X+1
            score = score + 3
        if Team2score > Team1score:
            print(Badteam[X],"wins, with a score of",Team2score,"against",Mainteam,"of",Team1score)
            X = X+1
            score = score + 1
        if Team2score == Team1score:
             print("ladies and gentlemen it's a tie, with",badteam[X]," score of",Team2score,"against",Mainteam,"score of",Team1score)
             X = X+1
             score = score + 2


    else:
         badteam.append(sidercharacter)

