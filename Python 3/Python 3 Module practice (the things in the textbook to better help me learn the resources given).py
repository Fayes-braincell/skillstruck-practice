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

file = open("Code Challenge Py 3.txt", "w")
file.write("In short, I love to code!")
file.close()

file = open("porcupine.txt", "w") v#Opening a new file with writing mode
#File Write Mode Code Challenge  

rows = 5
cols = 5
list = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(j)
    list.append(col)
print(list)