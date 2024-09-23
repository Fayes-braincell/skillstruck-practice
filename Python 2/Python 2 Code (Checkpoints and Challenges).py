
activities = ["movies", "skating", "bowling", "laser tag", "escape room", "trampoline park", "library"]

print(activities[:3])



activities[6] = "water park"

print(activities)

print(len(activities))
# Python Lists Continued code for checking for understanding'
#Supplimented from the "Code to get started" and ai


my_list = input("Enter names separated by spaces: ").split()

print(my_list[2] + " got the bronze medal") #Code for the Bronze Medal from Removing from Lists in Python (Code Challenges)
 
my_list = input("Enter different kinds of beans separated by spaces: ").split()

if "lima" in my_list:
    my_list.remove("lima")
print(my_list) #Code for Beans in the Removing from Lists in Python (Code challenges)



my_list = [int(n) for n in input("Enter in a list of numbers seperated by spaces: ").split()]
biggest = 0
for x in my_list:
    if x >= biggest:  
        biggest = x 

print(biggest)  
#Code for Code Challenges (Find the Largest Value)
#Genuinely causing me to lose hair just by looking at it

people_for_cats = 17

while people_for_cats > 0:
    print("There are " + str(people_for_cats) + " people interested in cats. That's good!")
    people_for_cats =  people_for_cats - 1

people_for_dogs = 20
while people_for_dogs > 0:
    print("There are " + str(people_for_dogs) + " people interested in dogs. That's cool!")
    people_for_dogs -= 1
#Code that is just meant to help me undertand what is expected of me for this module.
#Practicing how to use While Loops and how not to use them.


number = 1
while number <= 50:
    print(number)
    number += 1
 #Code for the Code checkpoint. Pretty simple code but I still needed the ai because it did confuse me just a little.



total = 0

number = int(input())

# Continue asking for input until the user enters 0
while number > 0:
    number != 0
    # Increment the total count
    total += 1
    # Receive the next integer input
    number = int(input("Enter an integer (0 to stop): "))

# Print the total number of numbers entered
print(total)
# Code for the How many numbers code challenge. Practically asking the user to input a bunch of numbers until 0 is entered to stop the program.

my_number = int(input("Pick a number: "))
total = 0

while my_number != 0:
    total += my_number
    my_number = int(input("Pick another number (0 to stop): "))

print(total)
#Code for the Sum of Numbers code challenge. Practically I'm having the user input a bunch of numbers untill it reaches whatever desired length, prompt them to use 0 to end the program so that the code will then use the total+= my_number to add all the numbers inputted together

def race():
    print("Phineas won the race")

race()

start = input("Would you like to launch the game? Enter yes or no: ")

def start_game():
    if start == "yes":
        print("Initialization Complete")
    else:
        print("Initialization Failed")

start_game()


def people(features):
    print("I really like people with " + features)

people("pretty smiles")
people("brown/hazel eyes")
people("curly hair") #Python Function Parameters code checkpoint


def odd_even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

odd_even(3) 
odd_even(10)
odd_even(7)  #Code for the Odd/Even Checking function Code challenge

month = int(input("Which month? 1-12: "))

def invitation(choice):
    if choice == 1 or choice == 3 or choice == 5 or choice == 7 or choice == 8 or choice == 10 or choice == 12:
        print("31")
    elif choice == 4 or choice == 6 or choice == 9 or choice == 11:
        print("30")
    elif choice == 2:
        print("28")
    else:
        print()

invitation(month) # Code for the Count the Days in a Month Function

def people(first, second):
    print("I really tend to gravitate towards people who " + first)
    print("I also really tend to gravitate towards people who " + second)

people("a similar sense of humor", "a soft and loving personality")
people("a nice sense of style", "a good taste in music") #Code Checkpoint for the Multiple Parameters in Python Functions


first = int(input("Choose a number: "))
second = int(input("Choose a number: "))
third = int(input("Choose a number: "))
fourth = int(input("Choose a number: "))
fifth = int(input("Choose a number: "))

def my_function(choice1, choice2, choice3, choice4, choice5):
    smallest = choice1
    if choice2 < smallest:
        smallest = choice2
    if choice3 < smallest:
        smallest = choice3
    if choice4 < smallest:
        smallest = choice4
    if choice5 < smallest:
        smallest = choice5
    print(smallest)

my_function(first, second, third, fourth, fifth)
# Code to Find the Smallest of Five Function


choice1 = int(input("What is the first number? "))
choice2 = int(input("What is the second number? "))

def my_function(first, second):
    if first < second:
        print(first)
    else:
        print(second)

my_function(choice1, choice2)
#Code for the Find the Smallest Integer Function code challenge


mountains = {
    "Everest" : 5,
    "Kilimanjaro" : 10,
    "Timpanogos" : 6,
    "Vesuvius" : 7,
}
mountains["Kilimanjaro"] = 22
print(mountains["Vesuvius"])
print(mountains)
#Code checkpoint for Dictionaries Module


unique_words = {
    "Ephemel" : "Lasting for a very short time; fleeting or transient.",
    "Serendipity" : "The occurrence of events by chance in a happy or beneficial way.",
    "Mellifluous" : "Pleasantly smooth and musical to hear; sweet-sounding.",
    "Limerence" : "The state of being infatuated or obsessed with another person, typically involving an intense emotional longing.",
    "Petrichor" : "The pleasant, earthy scent produced when rain falls on dry soil.",
    "Ineffable" : "Too great or extreme to be expressed or described in words.",
    "Quixtioc" : " Exceedingly idealistic; unrealistic and impractical, often in pursuit of noble but impossible goals.",
    "Solitude" : "The state or situation of being alone, often used to describe a peaceful or meditative",
    "Luminescence" : "The emmission of light by a substance that has not been heated, as in fluorenscence or phosphorescence.",
    "Ebullient" : "Cheerful and fully of energy",
}

print(unique_words)#Code for the Dictionary Author Code Challenge


colors = { 
    "red": 4, 
    "orange": 1, 
    "yellow": 2, 
    "green": 10, 
    "blue": 5, 
    "purple": 6
}

print(colors["orange"])
print(colors["purple"])

colors["red"] = 8
colors["blue"] = 15

print(colors) #Code for the Color Dictionary for Code Challenges. Just creating a dictionary named colors, adding 5 items to the dictionary, pulling two value keys and then replacing two values.

friends = {
    "Shane" : 10,
    "Samantha" : 9,
    "Shiloh" : 12,
    "Sean" : 11
}

print(friends)
friends["Sebastian"] = 8
friends.pop("Shiloh")
print(friends) #Code Checkpoint for Adding and Removing from Dictionaries


my_shape = input("What shape do you want to add?")
my_shape_height = int(input("How tall is your shape?"))

shapes = {
    "Triangle": 8,
    "Circle": 15,
    "Square": 10,
	"Rectangle" : 12,
}

shapes[my_shape] = my_shape_height 

print(shapes)#Code for the Arborist Code Challenge (Adding and Removing from a dictionary)

name = input("Which tree do you want to remove?")
trees = {
	"aspen" : 75,
	"pine" : 82,
	"maple" : 60,
	"oak" : 65,
	"willow" : 80,
	"cottonwood" : 100,	
}

trees.pop(name)
print(trees)#Code for the Arborist Code Challenge (Adding and Removing from a dictionary)

remove = input("What goal do you want to remove?")
goals = {
    "piano" : 5,
    "run" : 3, 
    "paint" : 2,
    "serve" : 7,
    "homework" : 7,
}

goals.pop(remove)
print(goals) #Code for the Goals Code challenge (Adding and Removing from a dictionary)

coins = {
    "pennies" : 6,
    "nickels" : 2,
    "dimes" : 3,
    "quarters" : 20
}
coins.pop("pennies")
coins["silver dollar"] = 0
print(len(coins)) #Code for the code checkpoint (Dictionaries Continued


dictionary = {
	1: "bicycle",
	2: "soccer balls",
	3: "piano books"
}

dictionary[4] = input("What do you have 4 of?")
dictionary[5] = input("What do you have 5 of?")
dictionary[6] = input("What do you have 6 of?")
print(dictionary) #Code for the How Many Code Challenge under the Dictionaries Continued Module


work = {

	"Monday": 3,
	"Tuesday": 4, 
	"Wednesday": 2,
	"Thursday": 1, 
	"Friday": 1, 
	
}

work["Saturday"] = 3
work.pop("Wednesday")
print(len(work))

if "Friday" in work:
	print("Friday is in work")

print(work) #Code for the Work Schedule Code Challenge under the Dictionaries Continued Module

#Hey...please find all the code you got you did from Looping through a dictionary onwards. You messed up big time for deleting all your code <3

cat_breeds = ("Siamese", "British shorthair", "Maine Coon", "Sphynx", "Burmese", "Birman", "Siberian", "Ragdoll" )

print(cat_breeds[-3])
print(cat_breeds[5])
print(cat_breeds[:4])

