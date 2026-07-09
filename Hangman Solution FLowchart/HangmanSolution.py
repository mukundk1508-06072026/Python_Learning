import random as rand
import webbrowser as webb
## the following are the rules of hangman 
##webb.open("https://en.wikipedia.org/wiki/Hangman_(game)")
## the above is the wikkipedia link to thenhangman game
# TODO 1 :-  Listing all the various words that make sense and putting it in a list 
# TODO 2:- Generating a random number 
# TODO 3:- Asking them to get a letter

animalList = ["camel","dog","cat","squirrel","tiger","wolf","lion","deer","mouse","pig","parrot"]
animal = rand.choice(animalList)
placeholders = ""
for position in range(0,len(animal)):
    placeholders += "_"
print(placeholders)
chances = len(animal)
status = False
print(f"you have {chances} lives")
correntLetters = []
while(chances>0):
    userGuess = input("Guess a letter: ").lower()
    display = ""
    ## here we need to check if the given letter is present /not 
    for char in animal:
        if(char == userGuess):
            display+=char
            correntLetters.append(userGuess)
        elif(char in correntLetters):
            display+= char
        else:
            display += "_"
    print(display)
    if(userGuess not in animal):
        chances = chances -1

    if(display.lower() == animal.lower()):
        status = True
        break
if(status == True):
    print("You Win") 
    print(f"{animal}")   
else:
    print(f"You lose. The word is {animal}")   