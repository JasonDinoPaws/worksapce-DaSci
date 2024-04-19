from sys import exit
from random import choice

class Game: # The Whole Game
    # All Settings that allow the game to function
    global Type,Length,Options,CAmount,Correct, OGP,Repeat, Guesses, Limit
    Type = 0
    Length = 4
    Options = ["r","o","g","y","bl","pu","pi","br","w"]
    CAmount = 6
    Correct = []
    Repeat = True
    Limit = 10

    # Updates Everytime a guess is made that is valid
    OGP = {
        "Incorrect": [],
        "WrongPlace": [],
        "Correct": []
    }
    Guesses = 0

    # Creates the Answer for this round
    def CreateAnswer():
        global Correct
        if Type == 1:
            print("\n\n\nCode Chooser")
        Correct = []
        
        for _ in range(Length):
            l = ""
            if Type == 1: # If Type is set to 1 which is 2 player
                print(f"\n{Options[0:CAmount]}")
                l = Choices(Options[0:CAmount],None,False)
            else:
                while True:
                    l = choice(Options[0:CAmount])
                    if Repeat or not l in Correct:
                        break
            Correct.append(l)
        if Type == 1:
            print("\n"*20)
    
    # Adds the color to a OGP array table for coloring to show what you have used
    def Marking(i,Spot):
        for a in ["Incorrect","WrongPlace"]:
           if i in OGP[a]:
                OGP[a].pop(OGP[a].index(i))
        if not i in OGP["Correct"]:  
            OGP[Spot].append(i) 
            
    # Checking The current Guess the player has made if it is correct
    def CheckGuess(Guess):
        global Guesses, OGP
        Replay = ""
        Guess = Guess.split(" ")
        CCopy = [] 
        for i in Correct:
            CCopy.append(i)

        if len(Guess) == Length: # Is the Length of the guess same as the property
            for i in range(len(Guess)):
                if Guess[i] in Options:

                    if Guess[i] in CCopy:

                        if Guess[i] == CCopy[i]: # If The Current Spot color the same as in the Correct Array
                            Game.Marking(Guess[i],"Correct")
                            Replay+= "\u001b[32m*\u001b[0m" # Adds the * to the replay and gives it a green color in the terminal
                            CCopy[i] = "^*)^*()^$%&*()#$^%&*()$^()&*#$^&*()#$^&*()^#$&*()#$^" # Spam so spot doesnt get reconized until another guess
                        else:
                            Game.Marking(Guess[i],"WrongPlace")
                            Replay += "\u001b[33m!\u001b[0m" # Adds the ! to the replay and gives it a yellow color in the terminal
                            CCopy[CCopy.index(Guess[i])] = "^*)^*()^$%&*()#$^%&*()$^()&*#$^&*()#$^&*()^#$&*()#$^" # Spam so spot doesnt get reconized until another guess


                    else:
                        Game.Marking(Guess[i],"Incorrect")
                        Replay += "\u001b[31m_ \u001b[0m" # Adds the _ to the replay and gives it a red color in the terminal
                else:
                    return f"{Guess[i]} is not a valid Guessing Option"
                
            Guesses+= 1
        else:
            Replay = f"Does not meet {Length}"
        return Replay
    
    # The Main thing to change the Settings and reset everything in the game
    def SettingChange(Data):
        global Type,Length,Options,CAmount,Correct, OGP,Repeat, Guesses, Limit
        Type = IsRequired(Data,"Type","int") and int(Data["Type"]) or 0
        Length = IsRequired(Data,"Length","int") and int(Data["Length"]) or 4
        Options = IsRequired(Data,"Options","array") and Data["Options"] or ["r","o","g","y","bl","pu","pi","br","w"]
        CAmount = IsRequired(Data,"CAmount","int") and int(Data["CAmount"]) or 6
        Repeat = IsRequired(Data,"Repeat","bool") and bool(Data["Repeat"]) or False
        Limit = IsRequired(Data,"Limit","int") and int(Data["Limit"]) or 10

        Correct = []
        OGP = {
        "Incorrect": [],
        "WrongPlace": [],
        "Correct": []
    }
        Guesses = 0

    # Mode Selection (Easy, Normal, Hard, Custom)
    def Select(mode = None):
        print("\n\n\n\n\n\n\n\n\nSelect a Mode\n")
        print("1 Easy (3 Letters, 4 colors, No Repeats, 15 Guesses)\n2 Normal (4 Letters, 6 colors, No Repeats, 10 Guesses)\n3 Hard (4 Letters, 10 colors, Contains Repeats, 5 Guesses)\n4 Custom (\033[1mCUSTOM\033[0m)")
        c = mode or Choices([1,2,3,4])

        if c == 1: # Easy
            Game.SettingChange({
                "Type": 0,
                "Length": 3,
                "CAmount": 4,
                "Repeat":False,
                "Limit":15,
            })
        elif c == 2: # Normal
            Game.SettingChange({
                "Type": 0,
                "Length": 4,
                "CAmount": 6,
                "Repeat":False,
                "Limit":10
            })
        elif c == 3: # Hard
            Game.SettingChange({
                "Type": 0,
                "Length": 6,
                "CAmount": 10,
                "Repeat":True,
                "Limit":5
            })
        elif c == 4: # Custom 
            Game.SettingChange({
                "Type": input("\n\n\nTwo Player (0: Solo,1: 2 player): "),
                "Length": input("Length (Number): "),
                "Options": input("Options (Array Table)(Word, Word): ").split(", "),
                "CAmount": input("Choose Amount (Number): "),
                "Repeat":input("Repeat (Boolean)(Only in Solo): "),
                "Limit": input("Guessing Limit (Number): ")
            })

        Game.Start(c)

    # The Core
    def Start(Mode):
        # Pre Loading 
        Game.CreateAnswer()
        print("\n"*20)
        if Type == 1:
            print("Guesser Turns")

        while True:
            # Adds all of the Options the Guess can pick from and adds color to the them if already guessed
            OptioText = ""
            for i in Options:
                OptioText += f"\u001b[{(i in OGP['Incorrect'] and 31) or (i in OGP['WrongPlace'] and 33) or (i in OGP['Correct'] and 32) or 37}m{i}\u001b[0m, "
            print(f"\nGuess #{Guesses+1}\n[{OptioText}\b\b]")

            Guess = Game.CheckGuess((input(f"Type a {Length} Letter Guess: ").lower()).strip()) # Guess

            if Guess == ("\u001b[32m*\u001b[0m"*Length): # Checks if the Guess was Correct 
                print(f"\n\u001b[32mYou Win\u001b[0m\nGuessing Amount: {Guesses}\n\n")
                break
            elif Guesses >= Limit: # Only Runs if the Guesses are at or over the limit
                print(f"\n\u001b[31mYou lose\u001b[0m\nCorrect Answer: ",end="")
                for i in Correct:
                    print(i,end=" ")
                print("\n\n")
                break
            else:
                print(f"\n{Guess}")

        # Replay Ability
        print("1 Play again in the same mode\n2 Play again in a diffrent mode\n3 Main Menu")
        c = Choices([1,2,3])
        if c == 1: # Same Mode Again with Same Settings
            Game.Select(Mode)
        elif c == 2: # Choose a Diffrent Mode 
            Game.Select()
        elif c == 3: # Main Meun
            LoadMainMenu()

# Just used in Settings to check the Settings that was being set was correct for what it was for
def IsRequired(self,text,type):
    if text in self:
        if type:
            try:
                if type == "int":
                    return int(self[text])
                elif type == "bool":
                    return bool(self[text])
                elif type == "array":
                    return isinstance(self[text], list) and len(self[text]) > 0 and self[text][0] != "" 
            except:
                return False
        else:
            return self[text]

# Guide 
def Guide():
    print("\n Welcome to the Guide. Select a Section\n"+("-"*10)+"\n")
    c = 0
    while c != 3:
        print("\n\n1 How to play\n2 Setting Meaning\n3 Main Menu")
        c = Choices([1,2,3])

        if c == 1: # How to play the game
            print("\n\nMaster mind is like wordle in some ways")
            print("Basically to beat it, you have to guess the colors combinated either set from the computer or other player")
            print("The Colors are in any range size depending on what mode you choose or set")
            print("You have a unimilited amount of tries to guess the correct order from the list of objects that is possible shown about where you type your guess\n")
            print("The responses use the following shorthand")
            print("\u001b[32m*\u001b[0m - correct color and location")
            print("\u001b[33m!\u001b[0m - correct color, incorrect location")
            print("\u001b[31m_\u001b[0m - neither")

        elif c == 2: # The Settings and what they do
            print("\n\nTwo Player\nWeather or not the game is solo or 2 Player\n")
            print("Length\nThe Size of how may colors you have to guess\n")
            print("Options\nThe whole list of stuff the guesser cna choose from\n")
            print("Choose Amount\nThe ammunt of stuff from the Options that it can choose from\n")
            print("Repeat\nWeather or not Repeat Options is allowed")
            print("Guessing Limit\nHow many tries the gusser has to solve the color combination")


    LoadMainMenu()

# The Choices Thing at the bottom of the screen (i.e
#  1 Play
#  2 Guide
#  2 Exit Game
#)
def Choices(AvalChoices,Convert = "int",AExit = True):
    if AExit:
        print(f"{AvalChoices[len(AvalChoices)-1]+1} Close Game")
        AvalChoices.append(AvalChoices[len(AvalChoices)-1]+1)
    c = 0
    while c == 0:
        try:
            c = IsRequired({"Text":input("Select: ")},"Text",Convert)
            if not c in AvalChoices:
                raise 
        except KeyboardInterrupt:
            c = AvalChoices[len(AvalChoices)-1]
            break
        except:
            c = 0
            print("Error Chooose again")
    if AExit and c == AvalChoices[len(AvalChoices)-1]:
        exit()
    return c


# Main Menu
def LoadMainMenu():
    print("\n"*20)
    print("1 Play\n2 Guide")
    c = Choices([1,2])
    
    if c == 1:
        Game.Select()
    elif c == 2:
        Guide()

LoadMainMenu()