#!/usr/bin/env python3
x = 0
first_Number = int(input("Enter the first number: "))
second_Number = int(input("Enter the second number: "))
result = first_Number * second_Number
print(first_Number ,"X" , second_Number,"=",result)
if result == 0:
    print("This result is positive and negative")
elif result > 0:
    print("This result is positive")
elif result < 0:
    print("This result is negative")
