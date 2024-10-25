#Multi-dimensional Lists

rows = 5
cols = 3
list = []
for i in range(rows):
    col = []
    for j in range(cols):
        list.append(5)
print(list) #Multi-dimensional Lists Code Checkpoint

first_names = ["James", "Cory", "Violet", "Faye"]
last_names = [" Bond", " Williams", " Dodgings", " Nwade"]
list = []
for i in range(first_names):
    first = []
    for j in range(last_names):
        list.append(first_names + last_names)
print(list) #Secret Agent Name Generator Code Challenge

rows = ["apple", "grape", "peach", "cinnamon", "vanilla"]
cols = input("Input a list of fruits").split()

list2 = []

for i in cols:
    col = []
    for j in rows:
        col.append(f"{i} {j}")
    list2.append(col)
    
print(list2) #Fruit Blender Code Challenge

#Iterating through 2D Lists
