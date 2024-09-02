activities = ["movies", "skating", "bowling", "laser tag", "escape room", "trampoline park", "library"]

print(activities[:3])



activities[6] = "water park"

print(activities)

print(len(activities))
# Python Lists Continued code for checking for understanding'
#Supplimented from the "Code to get started" and ai

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
