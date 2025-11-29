# This program takes names from user, writes in files and then read from it.

list_of_names = []

for i in range(1, 6):
    name = input("Enter name : ")
    list_of_names.append(name)


with open("File IO/names.txt", "w") as f:
    for name in list_of_names:
        f.write(name + "\n")

with open("File IO/names.txt", "r") as f:
    data = f.read()
    print(data)