# This code finds a value x inside a tuple

squares = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49
found = False

i = 0
while i < len(squares) :
    if (x == squares[i]) :
        print("Found at index",i)
        found = True
        break

    i += 1

if (found == False) : 
    print("Not found")