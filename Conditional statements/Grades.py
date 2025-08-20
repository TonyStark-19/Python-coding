# This program gives grades as per the marks

marks = int(input("Enter your marks : "))

if(100 >= marks >= 90):
    print("Grade A")
elif(marks < 90 and marks >= 80):
    print("Grade B")
elif(marks < 80 and marks >= 70):
    print("Grade C")
elif(marks >=0 and marks < 70):
    print("Grade D")
else:
    print("Enter valid marks only :(")