## checking if the environment is working / not.
'''print("Hello World")
print("This will be marking all the practice scripts and learnings related to python");
resources = "https://www.udemy.com/share/103J8C3@5X4F98BK-9gGlp3buD_tyLnpMinHJvQmUdsLddBftMp9ESSx2lcl2JJoqULUzSZl/"
print(resources);'''
###########################################################################################################################################
## Day 1 :- Printing, Commenting, Debugging, String Manupiulation and Variable Names.######################################################
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
print(f"You band name is {BandName}") ## this is an fstring'''
######################################################################################
## Day 2 => Data Types, Numbers, Operators, Type Conversion , f-strings ##############
## using the len() method we can get the number of characters in a string 
## Example:- 
'''char_len = len(input("Enter a string:- "));
print(f"Total character count {char_len}")'''
## Data Types :- 
## 1) String, 2) Integers, 3) Floats 4) Booleans

##strings => collection of characters => 
'''String = "Khamampati"
print(String[0]) ## this will give is the first letter of a string 
## string / array indexing starts with 0 
print(String[0:3])## gives you the first 3 characters in the said string
print(String[0:5:2])## gives you 3 characters such that there is a gap of 1 
## character in between each
print(String[-1])## when we use negative indices we are getting the string from the 
## reverse order so here i will be the result
print(String[-5:-1])## from the last 5th index to the last index this is how it works 
## Print behaviour ##
print("123"+"124")## concatenating 2 strings
print(123+124)## adding 2 numbers
print("123"+123)## here you must get a type error because you are trying to add a
## string and an integer which is incorrect because of the way they are occupied in the 
## memory.
print(12345+123.5)## here you can see that the int is being converted into float 
## and the addition takes place this is what we call upcasting and this is done
## by the interpretter.
print(12345 + int(12345.123))''' ## This is called downcasting becausr we are 
## explicitely tellling the interpretter to convert the float number into integer 
## effectively ignoring the decimal part of the equation.

## FUNCTION / METHODS => pretty simple a re-usable piece of code 
## You have input arguements and output.
'''print(type("Error"))
print(type(12345))
print(type(12.334))
print(type(True))'''
## type() is used to determine the data type of a variable / constant
## Operators in Python 
## '+,-,*,/,%',// => these are the arithematic operators 
## 'and, or,!' => Logical operators
## '>,<,=,=>,<=,!=' => relational operators
## '==' => asignment operatoes
## '**' this is generally for indicating power off
## all of these have a certain priority order and PEMDAS is something we use
## for mathematic operators 
## A Example :- Calculating the body mass index of a person
'''
height = float(input("Enter your height in meters:- "))
weight = float(input("Enter you weight in kilograms:- "))
bmi =((weight)/(height*height))
isUnhealthy = False
print(f"Your BMI is => {bmi}")
if(bmi>25.0 and bmi<29.9):
    print("You are over-weight")
    isUnhealthy =True
elif(bmi>18.5 and bmi<24.9):
    print("You are having a healthy weight")
elif(bmi>30.0):
    print("You are obese")
elif(bmi<18.5):
    print("You are underweight")
    isUnhealthy = True
## This is a condition to see if the given person needs to see a doc
if(isUnhealthy == True):
    print("Please see a doctor");
'''
## Mini Project :- Creating a tip calculator 
totalAmount = float(input("Please enter the total bill:- "));
isSplit = False;
toTip = bool(input("Do you want to tip the person? yes :- type 1 +Enter  no :- press Enter:- "))
if(toTip == True):
    tipPercentage = int(input("Please enter the tip percentage:- "))
    totalAmount = totalAmount*(tipPercentage/100) + totalAmount
    print(totalAmount);

toSplit = bool(input("Do you want to split the bill? yes :- type 1 +Enter  no :- press Enter:- "))
if(toSplit == True):
    split = int(input("How many people to split the bill:- "))
    isSplit = True
    totalAmount = totalAmount/split
    print(totalAmount)

if(isSplit == True):
    print(f"the amount per person amounts to  {totalAmount}");
else:
    print(f"Total amount to be paid is {totalAmount}")