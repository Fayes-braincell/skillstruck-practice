# Nested For Loops

rows = 3
pets = ["cats", "dogs", "rabbits", "fish", "snakes"]
list = [[j for j in pets] for i in range(rows)]

print(pets) #Code Checkpoint 

rows = int(input("How many rows do you want?"))
mylist = [1, 2, 3, 4, 5]
list = [[(j * rows) for j in mylist] for i in range(rows)]
print(list)#Multiply by the Number of Rows Code Challenge

rows = input("Input a list of weather").split()
cols = ["windy", "breezy", "calm"]
list =[[(i + " " + j) for j in cols] for i in rows]

print(list)
#Wather Watcher Code Challenge

#Multi-dimensional Lists

