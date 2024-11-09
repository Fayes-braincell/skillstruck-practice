
text_file = open("Code Challenge Py 3.txt", "r") 

print(text_file.read()) #Under the Reading Files Module (Code Checkpoint) and it doesn't pull up the text in the file so erm


file = open("cobra.txt",  "r")
print(file.read()) #Printing and reading the file at the same time #Secret Message Code Challenge 

file =  open("speech.txt", "r")
print(file.read())#Reading the Speech Code Challenge 

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

file = open("Code Challenge Py 3.txt", "r")
print(file.read(10))
print(file.readline())
print(file.readline())
file.close()
#Reading Parts of a File Code Challenge

number = int(input("How many characters do you want to print?"))
file = open("Code Challenge Py 3.txt", "r")
print(file.read(number))
file.close() #Read a Specific Number of Characters under the Reading Parts of a file Module

text_file = open("Code Challenge Py 3.txt", "r")
print(text_file.read())
text_file.split()
print(len(text_file))

file.close() #How many Words Code Challenge under the Reading Parts of a File Module. Wrote a program that prints out the number of words in a text file.

file =  open("Code Challenge Py 3.txt", "r")
print(len(file.readlines()))
file.close()
#How Many Lines Code Challenge under the Reading Parts of a File Module. Wrote a program that prints out the number of lines in a text file.

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

file = open("Code Challenge Py 3.txt", "a")
filename.write("I love programming!")
file.close()


file = open("Code Challenge Py 3.txt", "r")
print(file.read())#Appending a Line to a Text file Code Checkpoint

file =  open("letter.txt","a")
file.write("From your pen pal")
file.close()

file = open("letter.txt","r")
print(file.read()) #Pen pal Code Challenge under Append to Line to a Text File

file = open("report.txt", "a")
file.write("Quote was said by Gandhi")
file.close()

file = open("report.txt", "r")
print(file.read()) #Give Credit Code Challenge under the Append a Line to a Text File

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

file = open("Code Challenge Py 3.txt", "w")
file.write("In short, I love to code!")
file.close()

file = open("porcupine.txt", "w") #Opening a new file with writing mode
#File Write Mode Code Checkpoint 


file = open("email.txt", "w")
file.write("Never mind")
file.close() #Never Mind Code Challenge under the File Write Mode Module

answer = input("Enter what you want your greeting card to say")
file = open("report.txt", "w")

file.write(answer)
file.close()

file = open("report.txt", "r")
file.read()
print(file.read()) #Custom Greeting Cards Code Challenge under the File Write Mode
#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
 
x = int(input("What is the first number?"))
y = int(input("What is the second number?"))
z = int(input("What is the third number?"))


my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]

rows = 4
cols = 3

largest = 0

for i in range(rows):
	for j in range(cols):
         if my_list[i][j] > largest:
            largest = my_list[i][j]
print(largest) #Finding the Largest Value Code Challenge under the Iterating through 2D Lists Module
#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
class Dog:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size 
#Object-Oriented Programming Code Checkpoint

class Car:
    def __init__(self, kind, color, year):
        self.kind = kind
        self.color = color
        self.year = year
#Antique Car Show Code Challenge under the Object-Oriented Programming Module

class Tree:
    def __init__(self, fruit, height, leaf, flower, seed):
        self.fruit = fruit
        self.height = height
        self.leaf = leaf 
        self.flower = flower
        self.seed = seed
#Arborist Code Challenge under the Object-Oriented Programming Module

class Dessert:
    def __init__(self, shape, size, filling, topping):
        self.shape = shape
        self.size = size
        self.filling = filling
        self.topping = topping
#Bake Sale Code Challenge under the Object-Oriented Programming Module

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

class Hat:
    def __init__(self, kind, color, material):
        self.kind = kind
        self.color = color
        self.material = material
myObject = Hat("Beanie", "Black", "Wool")
#Creating an Instance Code Checkpoint


class Fruit:
    def __init__(self, shape, kind, size):
        self.shape = shape
        self.kind = kind
        self.size = size

fruit1 = Fruit("round", "apple", "medium")
fruit2 = Fruit("oblong", "banana", "large")
fruit3 = Fruit("oval", "mango", "medium")
fruit4 = Fruit("round", "orange", "small")

print(fruit1.kind)
print(fruit2.kind)
print(fruit3.kind)  
print(fruit4.kind) 
#A Fruit Festival Code Challenge under the Creating an Instance Module

class Pet:
    def __init__(self, name, color, origin):
        self.name = breed
        self.color = color
        self.origin = origin

pet1 = Pet("Siamese", "White and Brown", "Thailand")
pet2 = Pet("Budgerigar", "Multicolored", "Australia")
pet3 = Pet("German Shepherd", "Brown and Black", "Germany")
# Pet Store Code Challenge under the Creating an Instance Module

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

class Vacation:
    def __init__(self, place, distance, weather):
        self.place = place
        self.distance = distance
        self.weather = weather
    def tuesday(self):
        print("We will be hiking on Tuesday")

summer = Vacation("Hawaii", 2000, "Sunny")

summer.rating = 10
summer.weather = "rainy"

print(summer)
print(summer.rating)
print(summer.weather)
#Objects Continued Code Checkpoint

class Friday:
    def __init__(self, activity, friend):
        self.activity = activity 
        self.friend = friend
    def pictures(self):
        print("We took so many pictures")

thisWeekend = Friday("Movie", "Charlotte")

thisWeekend.money = 20

thisWeekend.friend = "Shane"

print(thisWeekend)
print(thisWeekend.money)
print(thisWeekend.friend)


class Shopping:
   
    def __init__(self, item, quality):
        self.item = item
        self.quality = quality
        self.total = []
        
    def spending(self, cost):
        self.total.append(cost)

# Create an instance of the Shopping class with specified arguments
sportStore = Shopping("Kayak", "High Quality")


sportStore.spending(100)
sportStore.spending(150)
sportStore.spending(200)

# Print the total list
print(sportStore.total)  # Output: [100, 150, 200]

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

stack = []

stack.append("Hi")
stack.append("Hello")
stack.append("Hey")
stack.append("Awe")

stack.pop("Awe")
print(stack)
#Stacks Code Checkpoint

first = "r"
second = "t"
third = "s"
fourth = "y"
fifth = "o"

stack = []

stack.append(third)
stack.append(second)
stack.append(fifth)
stack.append(first)
stack.append(fourth)

print(stack)
#Stack Scramble Code Challenge under the Stacks Module

response = input("What food should I bring?")

answer = ["apples", "steak", "potatoes", "carrots"]
if "s" in response:
    answer.append(response)
    print(answer)
else:
    print("The input doesn't have the letter s")
#Foods with the Letter S Coe CHallenge under the Stacks Module

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

this_list = ["Elephant", "Fossa", "Penguin", "Polar Bear", "Turtles", "Secretary Bird", "Axolotl", "Red Panda", "Okapi", "Shoebill Stork"]


def feeding(this_list):
    if len(this_list) == 1:
        print("The " + this_list[0] + " has been fed")
    else:
        mid = len(this_list) // 2
        first_half = this_list[:mid]
        second_half = this_list[mid:]

feeding(first_half)
feeding(second_half)

feeding(this_list)


#CAN YOU FUCKING REPASTE THE PAST CODE YOU FUCKING IDIOT. IT'S NOT THAT HARD TO DO YOU KNOB. anyway, repaste the lost code...

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

# Add a number from the user
num = int(input("Enter a number to add to the list: "))
arr.append(num)

def mergeSort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        L = sort_list[:mid]
        R = sort_list[mid:]
        
        # Recursively sort both halves
        mergeSort(L)
        mergeSort(R)

        # Initialize variables for merging
        i = j = k = 0

        # Merge sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sort_list[k] = L[i]
                i += 1
            else:
                sort_list[k] = R[j]
                j += 1
            k += 1

        # Append remaining elements from L
        while i < len(L):
            sort_list[k] = L[i]
            i += 1
            k += 1

        # Append remaining elements from R
        while j < len(R):
            sort_list[k] = R[j]
            j += 1
            k += 1
    
    return sort_list

# Sort the list with the user's added number
sorted_list = mergeSort(arr)
print(sorted_list)

