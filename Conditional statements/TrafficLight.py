# This code checks traffic light and prints it's respective output

light = input("Enter color of light : ")

if(light == "red"):
   print("Stop!!!")
elif(light == "yellow"):
   print("Look around")
elif(light == "green"):
   print("gooo!!!")
else:
   print("Light is broken :(")