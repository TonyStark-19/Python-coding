# This code searches in which line does the word "learning" occurs first in the file practice.txt

# to create file
# with open("File IO/Practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

def check_for_line(word):
    data = True
    line_no = 1

    # read file
    with open("File IO/Practice.txt", "r") as f:
        # read line by line
        while data:
            data = f.readline()
            if(word in data):
                return line_no
            line_no += 1
        
    return -1

# call function
result = check_for_line("learning")

if result != -1:
    print(f'Word found on line {result}')
else:
    print("Word not found")