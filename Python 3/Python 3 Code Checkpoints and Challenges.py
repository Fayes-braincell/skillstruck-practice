
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

#{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

file = open("email.txt", "w")
file.write("Never mind")
file.close() #Never Mind Code Challenge under the File Write Mode Module

answer = input("Enter what you want your greeting card to say")
file = open("report.txt", "w")

file.write(answer)
file.close()

file = open("report.txt", "r")
file.read()
print(file.read())