#Reading Files

file = open("Code Challenge Py 3.txt", "r") 
print(file.read()) #Reading Files Noted code (gave me a headache because it doesn't actually open the file, as it says its not in the directory...understandable

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

#Reading Parts of a file

file = open("Code Challenge Py 3.txt", "r")
print(file.read(5)) #This prints out 5 characters from the text file
#Reading/printing an amount of characters

file = open("Code Challenge Py 3.txt", "r")
print(file.readline())
#To print multiple lines from a text file using print(file.readline()), you need to repeat the command for each line you want to print.

file = open("Code Challenge Py 3.txt", "r")
print(file.readlines()) #This line of code would print out all lines of code in the text file

file.close() #Closes the file you opened

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

#Append a Line to a Text File

file = open("Code Challenge Py 3.txt", "r")
file.write("You like it when I'm rough")
file.close() #Appending a line to a text file

file = open("Code Challenge Py 3.txt", "r")
file.write("You like it when I'm rough")
file.close()

file = open("Code Challenge Py 3.txt", "r")
print(file.read()) #Reading the text file to see if the appended line worked

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{{}{}{}{}{}{}{}{}{}{}{}{}

file = open("Code Challenge Py 3", "w")
file.write("I want to buy you something, but I don't have any money. No I don't have any money")
file.close() #Using Writing mode. Write mode and append mode are similar but the difference between them is the fact that writting mode replaces all the text in the file

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
rows = 5
cols = 5
list = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(j)
    list.append(col)
print(list) #Creating a 2D List in Nested For Loops

list = ["hello" for i in range (5)]
print(list) #This code will create a list that is 5 indexes long, with hello as the value in all the indexes

rows = 3 
my_list = [1, 2, 3, 4, 5]
list = [[j for j in my_list] for i in range(rows)]

print(list) #Creating one line nested for loops to create multi-dimensional lists. 

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
n = 5
lists = []
for i in range(n):
    list.append(0)
print(lists) #Creating a one-dimentional list

rows = [4, 6, 8,]
cols = ["lilac", "beige", "sage green", "saphire"]
list = []
for i in rows:
    col = []
    for j in cols:
        col.append(j)
    list.append(col)
print(list) #Making a 2D lists

rows = 5
cols = 5
list = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(i)
    list.append(col)
print(list) #This code uses one for loop to create the columns, and another for loop to create the rows for the columns (nested for loops)
#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

my_list = [[0, 1, 2,], [10, 15, 20], [100, 200, 300],
[5, 6, 7]]
rows = 4
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list * 2 #Thi line of code will multiply each element of a 2D list by 2

print(my_list) 
#Anoher examle
my_list = [["dog", "cat", "frog"], ["shark", "squid", "whale"], ["deer", "fox", "badger"]]
rows = 3
cols = 3


for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] + " is awesome"

print(my_list) #Code block concantenates "is awesome" the elements in the 2D list
#Lesson is Iterating Through 2D Lists

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

#Lesson is Oject-Oriented Programming


class Person:
    def __init__(self, name, age, gender):#There are two underscores on each side with the initialize function. The initialize function must have a self parameter and with it comes attributes you want the class to have.
        self.name = name
        self.age = age
        self.gender = gender #Has to be one of these assignments for each attribute of the class.
#**A class is a bluprint of an object**

#Instances - It's basically specific information that relates to you that you write down on a form. That would be an instance of the class. They are actual objects created by classes, and the instance is created by an actual person.

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

#Lesson : Creating an Instance/Object

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person("Faye", "17", "Nonbinary")

print(p1) #when you print p1, it returns the reference of that object and doesn't return the attributes but to do that you calling the object name and the attribute: p1.attribute

class Person: 
    def __init__(self,name, age, gender):
        self.name = age
        self.age = age
        self.gender = gender
    
p1 = Person("Faye", "17", "Nonbinary")
print(p1.name)

#You can concatenate different parts of the object too

p1 = Person("Faye", "17", "Nonbinary")#*Taking from the final 2 lines of the block of code
print("This is: " + p1.name + "." + " They are: " + p1.age + "." + " They are: " + p1.gender) #This is more complicated than the textbook but I needed to customize it to make the point a little more obvious

class Person: 
    def __init__(self,name, age, gender):
        self.name = age
        self.age = age
        self.gender = gender
    
p1 = Person("Faye", "17", "Nonbinary")
p2 = Person("Aniya", "16.5", "Female")

print(p1.name)
print(p2.gender)
print(p1.age)
print(p1.gender)
print(p2.name) #Having access to the information of the objects and printing them in whatever order we need it in
