# This code check if the elements of the List forms a palindromic pattern or not

list1 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("List is a palindrome")
else: 
    print("List is not a palindrome")