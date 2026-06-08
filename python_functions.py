# ==========================================
# FUNCTIONS, ARGUMENTS, RETURN VALUES
# MATH, RANDOM, DATETIME MODULES
# ==========================================

import math
import random
from datetime import datetime

# ------------------------------------------
# 1. Simple Function
# ------------------------------------------
def welcome():
    print("Welcome to Python Functions Program")

welcome()

# ------------------------------------------
# 2. Function with Arguments
# ------------------------------------------
def greet(name):
    print("Hello,", name)

greet("Suresh")

# ------------------------------------------
# 3. Function with Return Value
# ------------------------------------------
def add(a, b):
    return a + b

result = add(10, 20)
print("\nAddition =", result)

# ------------------------------------------
# 4. Function to Find Maximum Number
# ------------------------------------------
def find_max(x, y):
    if x > y:
        return x
    else:
        return y

print("Maximum Number =", find_max(25, 15))

# ------------------------------------------
# 5. Math Module Functions
# ------------------------------------------
number = 25

print("\n----- MATH MODULE -----")
print("Square Root:", math.sqrt(number))
print("Power:", math.pow(5, 3))
print("Ceiling:", math.ceil(5.2))
print("Floor:", math.floor(5.8))
print("Factorial:", math.factorial(5))
print("Pi Value:", math.pi)

# ------------------------------------------
# 6. Random Module Functions
# ------------------------------------------
print("\n----- RANDOM MODULE -----")

print("Random Integer:", random.randint(1, 100))
print("Random Float:", random.random())

colors = ["Red", "Green", "Blue", "Yellow"]
print("Random Choice:", random.choice(colors))

# ------------------------------------------
# 7. Datetime Module Functions
# ------------------------------------------
print("\n----- DATETIME MODULE -----")

current = datetime.now()

print("Current Date & Time:", current)
print("Year:", current.year)
print("Month:", current.month)
print("Day:", current.day)
print("Hour:", current.hour)
print("Minute:", current.minute)
print("Second:", current.second)

# ------------------------------------------
# 8. Function with User Input
# ------------------------------------------
def calculate_square(num):
    return num ** 2

n = int(input("\nEnter a Number: "))
print("Square =", calculate_square(n))

# ------------------------------------------
# 9. Function for Even/Odd Check
# ------------------------------------------
def check_even_odd(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

number = int(input("Enter Another Number: "))
print(check_even_odd(number))

# ------------------------------------------
# 10. Function for Factorial
# ------------------------------------------
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact

num = int(input("Enter Number for Factorial: "))
print("Factorial =", factorial(num))

# ------------------------------------------
# 11. Function Returning Multiple Values
# ------------------------------------------
def calculations(a, b):
    return a + b, a - b, a * b, a / b

sum1, sub1, mul1, div1 = calculations(20, 10)

print("\n----- MULTIPLE RETURNS -----")
print("Addition =", sum1)
print("Subtraction =", sub1)
print("Multiplication =", mul1)
print("Division =", div1)

# ------------------------------------------
# 12. Lambda Function
# ------------------------------------------
square = lambda x: x * x

print("\nLambda Square of 5 =", square(5))

print("\nProgram Completed Successfully!")