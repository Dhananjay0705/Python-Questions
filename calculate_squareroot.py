# solution 1) Using Exponentiation operstor

# num = 65
num1 = float(input("Enter a number to find the square root : "))

sr = num1**(1/2)
print("Square root of the given number is : ",sr)

## Solution 2) Using math module

import math ## math = Module

num1 = float(input("Enter a number to find the square root : "))

sr = math.sqrt(num1)

print("Square root of the given number is : ",sr)

 