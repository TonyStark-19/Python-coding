# This program shows how to delete files in python

# create files
# with open("File IO/Practice.txt", "w") as f:
#     f.write("Example text")
#     print("File created")

# import os module
import os

# delete file
os.remove("File IO/Practice.txt")
print("File deleted!")