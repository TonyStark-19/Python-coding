# This code stores marks with subjects in a dictionary

marks = {}

x = int(input("Enter phy : "))
marks.update({"phy" : x})

x = int(input("Enter math : "))
marks.update({"math" : x})

x = int(input("Enter chem : "))
marks.update({"chem" : x})

print(marks)