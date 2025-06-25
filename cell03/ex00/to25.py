#!/usr/bin/env python3
print("Enter a number less than 25")
user_inp = int(input())
if(user_inp <= 25):
 while user_inp <= 25:
  print(f"Inside the loop, my variable is {user_inp}")
  user_inp += 1 
else:
 print("Error")