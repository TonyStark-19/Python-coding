# This code replaces all occurences of java with python in the file practice.txt

# to create file
# with open("File IO/Practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

# read file
with open("File IO/Practice.txt", "r") as f:
    data = f.read()

# replace values
newData = data.replace("Java", "Python")

# and then change the values in file
with open("File IO/Practice.txt", "w") as f:
    f.write(newData)