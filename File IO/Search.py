# This code searches if the word "learning" exists in the file practice.txt or not

# to create file
# with open("File IO/Practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

# read file
def check_for_word(word):
    with open("File IO/Practice.txt", "r") as f:
        data = f.read()

        # check if word exits or not
        if(word in data):
            print("Found")
        else:
            print("Not found")

# call function
check_for_word("learning")