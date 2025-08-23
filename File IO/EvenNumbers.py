# This code returns the count of even numbers

# to create file
# with open("File IO/Practice.txt", "w") as f:
#     f.write("1, 2, 76, 84, 90, 101")

count = 0
# read file
with open("File IO/Practice.txt", "r") as f:
    data = f.read()

    # splid it into list
    nums = data.split(",")
    for val in nums:
        # check even
        if(int(val) % 2 == 0):
            count += 1

# print count
print(count)