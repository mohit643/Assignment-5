""" Write a python script which takes a three digit number from the user and displays
only its first digit. """

"""a=int(input("Enetr Any Three Digit Number:- "))
while(a>=10):
  a=a//10
print("First Digit is:- ",a)"""

a=int(input("Enetr Any Three Digit Number:- "))
b=a//100
print(int(b))
  