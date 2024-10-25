#Iterating through 2D Lists
my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]
rows = 5
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] + 3

print(my_list) #Iterating through 2D Lists Code Checkpoint

my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
multiply = int(input("Enter in a number you want all the elements in the 2D List"))
rows = 4
cols = 3


for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] * multiply

print(my_list) #Multiply List Values Code Challenge

