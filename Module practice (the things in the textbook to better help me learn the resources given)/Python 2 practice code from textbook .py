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



