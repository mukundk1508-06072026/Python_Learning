## checking if the environment is working / not.
'''print("Hello World")
print("This will be marking all the practice scripts and learnings related to python");
resources = "https://www.udemy.com/share/103J8C3@5X4F98BK-9gGlp3buD_tyLnpMinHJvQmUdsLddBftMp9ESSx2lcl2JJoqULUzSZl/"
print(resources);'''
###########################################################################################################################################
## Day 1 :- Printing, Commenting, Debugging, String Manupiulation and Variable Names.
## print => used to print your onto the console. Pretty useful for debugging at timees
## String => set of characters or say an array of characters;
## Syntax error => its generally indicated with red. tells you that you have messed up 
## so check your code again. 
'''print(hello world)'''
## here you can see that we did not enclose HELLO WORLD in double quotes hence we are getting an error here
## resources to go to when we make errors 1) Stack OverFlow and 2) ChatGPT/Gemini
## This is Typically how print statements are used here
'''print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")'''


## String Manipulations ##
## to print things multiple times we can either used multiple print statements/use 1 print statemrnt and write the contents with 
## an escape character => '\n' or use a Loop (which is what sane people do);

## Method1.
'''print("Hi")
print("Hi")
print("Hi")'''

## Method2 => in this method we are using string manupilation.
'''print("Hi\nHi\nHi");'''

## Method3.
'''for i in range(0,1,3):
    print("Hi\n")'''

## String Concatenation => taking separate strings and merging them into one.
## Example:-
'''firstName = "Mukund"
secondName = "Khamampati"
fullName = "Mukund"+" "+"Khamampati" ## here two strings are being concatenated.
print(fullName)'''
## In compiled langugaes like C,C++ and C# (These are the ones I have stidied earlier)
## '{}' indicate the start and end of a given block of code.
## in python indentation which is a 'TAB' space is something similar to that .
## been demonstrated in Method3


## Taking User Input
'''print("Please give me some input") ## this is for printing on the console
variable = input("Please provide a valid input:- ")## this is you input and storing it in varibale
print(variable)'''
## here we use variable ; think of it as a container or say a BOX
## in compiled languages the variable 's data type must be defined but here its
## not needed. Python is an interpretter based language meaning here 
## since I am on a linux system the BASH has an built "python3" interpretter which 
## runs script "Learnings.py" in my case.
## Naming can be done in the follwing conventions
## 1) Camel Case 2) Snake Case 3) Pascal Case and I will be following camel case 
## Variable Names must actually make sense and there must be a reason to call a variable
## a certain way 
## swaping to number/entities with a 'temp variable
'''glass1 = "milk"
glass2 = "juice"
print(glass1,glass2)
temp = glass1
glass1 = glass2
glass2 = temp
print(glass1,glass2)'''
## while declaring variable we do not use 'var' like we do while we declare dynamic type 
## variables in C#

### Small Project :- BAND NAME GENERATOR##
'''print("Welcome to a Band Name Generator")
City  = input("Enter the city that you have grown up in:- " )
Pet_Name = input("Enter a pet NAME :- ")
BandName = City+" "+Pet_Name
print(f"You band name is {BandName}")'''
######################################################################################

