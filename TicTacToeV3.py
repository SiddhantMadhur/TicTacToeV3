#@author: SiddhantMadhur
import os

tl = " "        #table and var defined here:
tm = " "
tr = " "
ml = " "
mm = " "
mr = " "
bl = " "
bm = " "
br = " "
emp = "Empty Var do not change"
table = [emp, bl, bm, br, ml, mm, mr, tl, tm, tr]

#define functions here
def debug(errorCode, comment): #easier to debug in post
    if errorCode == 100:
        print("There has been an error with the code. Please contact me. ")
    elif errorCode == 101:
        print("There was a user error. Please Make sure to use the correct syntax provided. Additional Details: " + comment)

def showTable():
    print(" " + table[7] + " | " + table[8] + " | " + table[9] + " ")
    print(" " + table[4] + " | " + table[5] + " | " + table[6] + " ")
    print(" " + table[1] + " | " + table[2] + " | " + table[3] + " ")

def checkWin(checker): #old system i brought here. couldnt think of anything better and it is 2:46am so I will absolutely not.
    streak = False
    if table[7] == checker and table[8] == checker and table[9] == checker: 
        streak = True
    elif table[4] == checker and table[5] == checker and table[6]: 
        streak = True
    elif table[1] == checker and table[2] == checker and table[3] == checker: 
        streak = True
    elif table[1] == checker and table[4] == checker and table[7] == checker: 
        streak = True
    elif table[2] == checker and table[5] == checker and table[8] == checker:
        streak = True
    elif table[3] == checker and table[6] == checker and table[9] == checker:
        streak = True
    elif table[3] == checker and table[5] == checker and table[7] == checker: 
        streak = True
    elif table[9] == checker and table[5] == checker and table[1] == checker:
        streak = True
    
    if streak == True:
        SystemExit

    return streak
#         
#end of function definitions
#
#start of actual code:

p1 = input("Hey Player 1, whats your name?\n")
p2 = input("Alright " + p1 + ", Hey Player2 whats your name? \n")
print("Which player wants to go first?")
inp1 = input()
player = ["", ""]
if inp1 == "X" or inp1 == "x":
    player[0] = "X"
    player[1] = "O"
elif inp1 == "O" or inp1 == "o":
    player[0] == "O"
    player[1] == "X" 

for round in range(10): #this is the rounds
    round = round + 1    
    if round%2!=0:
        x = 0
    else:
        x = 1

    print("Round " + str(round) + ": Choose your placement, " + player[x])
    inp2 = int(input())
    print("\n")
    if (table[inp2] == " "):
        table[inp2] = player[x]
    else:
        print("Somebody already placed here.")
        round = round - 2
    showTable()
    if checkWin(player[x]) == True:
        print("Game ended, " + player[x] + " won!")
        exit()
    print("\n")
print("Looks like the game tied.")
os.system("pause")