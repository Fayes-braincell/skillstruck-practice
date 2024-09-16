#Python 2 Section

def weather():
    print("It's a soggy day outside!")

weather()
#Other code that have been found under this module are in my notes on paper. Explanations to them are also added.

#Parameters: the things that go inside the function parenthesis. They also go inside the function declaration.

def weather(type): 
    print("It's a soggy day outside because it is " + type)

weather(" a sad day") #code is not particularily working but it's on the textbook sooooo, probably a step in the sand

#Arguments, just adding in an argument in the string and then calling the function multiple times with different parameters.
def weather(forecast):
    print("Its's a soggy day outside because it is " + forecast)

weather("raining")
weather("drizzling")
weather("snowing")

#Multiple Parameters in Python Functions. Functions can accept more than one parameter

def gifts(first, second):
    print("Your first choice for a birthday gift would be " + first)
    print("Your second choice for a birthday gift would be " + second)

gifts("bike", "basketball")
gifts("speaker", "tickets")

#Local and Global Scioe Variables. Sometimes you want to create a variable inside a function and that would be called local variable (Can only used inside the function.)


favorite = "I love juice"
def myfunction():
    fruit= "apple"
    print(fruit)

myfunction()

print(favorite) #In thi example, fruit is the local variable. This was covered in a different module but still is important to what you're learning right now.

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

#Learning dictionaries: They are ordered, changeable, and indexed.

classmates = {
    "Cory" : 8,
    "Andre" : 12,
    "Dareon" : 10
}
print(classmates)
 #This code uses integers as the values


names = {
     "person1" : "Jaquan",
     "person2" : "Andrian", 
     "person3" : "Catherina",
     "person4" : "Aaliyah",
}
print(names)
#This code uses strings as the values for the keys


classmates = {
    "Cory" : 8,
    "Andre" : 12,
    "Dareon" : 10
} 
print(classmates["Andre"])
#This code accesses items from the dictionaries


classmates = {
    "Cory" : 8,
    "Andre" : 12,
    "Dareon" : 10
}
classmates["Andre"] = 21
print(classmates) #This code allows you to change the values in the dictionary

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

classmates = {
    "Cory" : 8,
    "Andre" : 12,
    "Dareon" : 10,
}
classmates["Yaliyah"] = 15

print(classmates) #Adding things/items to a dictionary


friends = {}

friends["Aniya"] = 10
friends["Tiffany"] = 12

print(friends) #Adding into an empty dictionary


classmates = {
    "Cory" : 8,
    "Andre" : 15,
    "Dareon" : 10,
    "Violet" : 12,
    "Dahlia" : 6
}
print(classmates)
classmates.pop("Dareon")
print(classmates) #Removing Items from a dictionary

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

classmates = {
    "Cory" : 8,
    "Andre" : 15,
    "Vance" : 10,
    "Dareon" : 6,
    "Violet" : 12
}

print(len(classmates)) #Checking Dictionary Length


classmates = {
    "Cory" : 8,
    "Andre" : 15,
    "Vance" : 10,
    "Dareon" : 6,
    "Violet" : 12
}

if "Andre" in classmates:
    print("Andre is in your dictionary")

classmates = {
    "Cory" : 8,
    "Andre" : 15,
    "Vance" : 10,
    "Dareon" : 6,
    "Violet" : 12
}

if "Darrell" not in classmates:
    print("Darrell is not in your dictionary") #Checking if a key is in your dictionary


garden = ["spinach", "wheat", "tomatoes", "potatoes"]

garden_dictionary = dict.fromkeys(garden, "Harvested")
print(garden_dictionary) #Converting from a Python list to a dictionary

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

classmates = {
    "Cory" : 8,
    "Andre" : 15,
    "Vance" : 10,
    "Dareon" : 6,
    "Violet" : 12
}
for x in classmates:
    print(x) #Printing out the key names when Looping Through a Dictionary

classmates = {
    "Cory" : 8,
    "Andre" : 15,
    "Vance" : 10,
    "Dareon" : 6,
    "Violet" : 12
}

for x in classmates.values():
    print(x) #Printing out the values of a dictionary when Looping Through a Dictionary


classmates = {
    "Cory" : 8,
    "Andre" : 15,
    "Vance" : 10,
    "Dareon" : 6,
    "Violet" : 12
}
for x,y in classmates.items():
    print(x,y) #Printing out both keys and values when Looping Through a Dictionary

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

classmates = {
    "Cory" : 8,
    "Andre" : 15,
    "Vance" : 10,
    "Dareon" : 6,
    "Violet" : 12
}

for x in classmates:
    if x == "Andre":
        print("This person wants to be anonymous")
    else:
        print(x) #The loop runs through each student's name and checks to see if there is an Andre and if there is, it will print out the if statement associated to it. If there is no Andre, then it will print out the whole list as it is
#E.g 
classmates = {
    "Cory" : 8,
    "Andre" : 15,
    "Vance" : 10,
    "Dareon" : 6,
    "Violet" : 12
}
for x in classmates:
    if x == "John":
        print("This person wants to remain anonymous")
    else:
        print(x) #Is the extra example that goes with the code above.


periods =  int(input("How many class periods do you have?"))
schedule = {}
for i in range(periods):
    subject =  input("what's the subject")
    num_people = input("How many people are in your " + subject + " class?")
    if subject not in schedule:
        schedule[subject] = num_people
print(schedule)
#Using a For Loop to Create a Dictionary, notes for this specific code is in physical notes

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

#Tuples are unchangeable!! They use parentheis instead of square brackets like a lists would.

instruments = ("clarinet", "piano", "drum", "violin")

print(instruments)

instruments = ("clarinet", "piano", "drum", "violin")

print(instruments[1]) #Accessing Tuple Items. This will print out piano

instruments =  ("clarinet", "piano", "drum", "violin")

print(instruments[-1]) #Negative Indexing

instruments = ("clarinet", "piano", "drum", "violin")

print(instruments[1:3]) #Range of Indexes. You can use a range with one simple command to access multiple values
#Things that you can't do to Tuples
# - Change Items in them
# - Add to them
# - Remove from them
# You'd use a tuple when you need an ordered, immutable collection of items that should stay constant, and in situations where immutability helps with memory optimization or ensures data integrity. (the use for them)

instruments =  ("clarinet", "piano", "drum", "violin", "guitar")

if "piano" in instruments:
    print("The tuple contains the value of piano.")
else:
    print("The tuple does not contain the value of piano") #Checking if an Item exists in the tuple - using a simple if statement

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}