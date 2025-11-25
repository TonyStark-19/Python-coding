# This program demonstrates the use of match-case statements in Python. 

color = input("Enter a color: ")

match color.lower():
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case "yellow":
        print("Look out")
    case _:
        print("Enter a valid traffic Light color :(")