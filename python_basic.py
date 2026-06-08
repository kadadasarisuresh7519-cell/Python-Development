# ==========================================
# PYTHON BASICS TO ADVANCED - ALL IN ONE
# ==========================================

# 1. USER INPUT
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# 2. VARIABLES AND DATA TYPES
college = "ABC College"      # String
cgpa = 8.5                   # Float
is_student = True            # Boolean

print("\n----- STUDENT DETAILS -----")
print("Name:", name)
print("Age:", age)
print("College:", college)
print("CGPA:", cgpa)
print("Student:", is_student)

# 3. OPERATORS
a = 20
b = 10

print("\n----- OPERATORS -----")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# 4. CONDITIONAL STATEMENTS
print("\n----- IF ELSE -----")
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# 5. ELIF EXAMPLE
marks = int(input("\nEnter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# 6. FOR LOOP
print("\n----- FOR LOOP -----")
for i in range(1, 6):
    print(i)

# 7. WHILE LOOP
print("\n----- WHILE LOOP -----")
count = 1
while count <= 5:
    print(count)
    count += 1

# 8. LIST
print("\n----- LIST -----")
fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

for fruit in fruits:
    print(fruit)

# 9. FUNCTION
print("\n----- FUNCTION -----")

def add(x, y):
    return x + y

result = add(10, 20)
print("Sum =", result)

# 10. FACTORIAL USING LOOP
print("\n----- FACTORIAL -----")

num = int(input("Enter a Number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

# 11. MULTIPLICATION TABLE
print("\n----- TABLE -----")

n = int(input("Enter Number for Table: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# 12. PATTERN PROGRAM
print("\n----- STAR PATTERN -----")

for i in range(1, 6):
    print("*" * i)

# 13. EVEN ODD CHECK
print("\n----- EVEN ODD -----")

number = int(input("Enter Number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("\nProgram Completed Successfully!")