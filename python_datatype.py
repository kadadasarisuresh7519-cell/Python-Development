# ==========================================
# LISTS, TUPLES, DICTIONARIES, SETS
# AND LIST COMPREHENSIONS
# ==========================================

# ------------------------------------------
# 1. LIST OPERATIONS
# ------------------------------------------

print("----- LIST OPERATIONS -----")

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

# Add element
fruits.append("Orange")
print("After Append:", fruits)

# Insert element
fruits.insert(1, "Grapes")
print("After Insert:", fruits)

# Remove element
fruits.remove("Banana")
print("After Remove:", fruits)

# Update element
fruits[0] = "Pineapple"
print("After Update:", fruits)

# Length of list
print("Length:", len(fruits))

# Traversing list
print("List Elements:")
for fruit in fruits:
    print(fruit)

# ------------------------------------------
# 2. NESTED LIST
# ------------------------------------------

print("\n----- NESTED LIST -----")

students = [
    ["Suresh", 22],
    ["Ravi", 21],
    ["Priya", 20]
]

for student in students:
    print(student)

# ------------------------------------------
# 3. TUPLE HANDLING
# ------------------------------------------

print("\n----- TUPLE HANDLING -----")

student = ("Suresh", 22, "Python")

print("Tuple:", student)
print("Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])

# Tuple unpacking
name, age, course = student

print("\nTuple Unpacking")
print(name)
print(age)
print(course)

# ------------------------------------------
# 4. DICTIONARY USAGE
# ------------------------------------------

print("\n----- DICTIONARY -----")

employee = {
    "id": 101,
    "name": "Suresh",
    "salary": 50000
}

print("Dictionary:", employee)

# Access value
print("Name:", employee["name"])

# Add new key
employee["department"] = "IT"

# Update value
employee["salary"] = 60000

print("Updated Dictionary:", employee)

# Loop through dictionary
print("\nDictionary Items")

for key, value in employee.items():
    print(key, ":", value)

# ------------------------------------------
# 5. NESTED DICTIONARY
# ------------------------------------------

print("\n----- NESTED DICTIONARY -----")

students = {
    1: {"name": "Suresh", "age": 22},
    2: {"name": "Ravi", "age": 21}
}

for roll, details in students.items():
    print(roll, details)

# ------------------------------------------
# 6. SET OPERATIONS
# ------------------------------------------

print("\n----- SET OPERATIONS -----")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set1:", set1)
print("Set2:", set2)

# Union
print("Union:", set1 | set2)

# Intersection
print("Intersection:", set1 & set2)

# Difference
print("Difference:", set1 - set2)

# Symmetric Difference
print("Symmetric Difference:", set1 ^ set2)

# Add element
set1.add(10)

print("After Add:", set1)

# ------------------------------------------
# 7. LIST COMPREHENSIONS
# ------------------------------------------

print("\n----- LIST COMPREHENSION -----")

numbers = [1, 2, 3, 4, 5]

# Squares
squares = [num ** 2 for num in numbers]

print("Numbers:", numbers)
print("Squares:", squares)

# Even Numbers
evens = [num for num in range(1, 21) if num % 2 == 0]

print("Even Numbers:", evens)

# Odd Numbers
odds = [num for num in range(1, 21) if num % 2 != 0]

print("Odd Numbers:", odds)

# ------------------------------------------
# 8. ADVANCED LIST COMPREHENSION
# ------------------------------------------

print("\n----- ADVANCED LIST COMPREHENSION -----")

names = ["suresh", "ravi", "priya"]

capitalized = [name.upper() for name in names]

print("Original Names:", names)
print("Capitalized Names:", capitalized)

# ------------------------------------------
# 9. COMBINED EXAMPLE
# ------------------------------------------

print("\n----- COMBINED EXAMPLE -----")

students = [
    {"name": "Suresh", "marks": 85},
    {"name": "Ravi", "marks": 72},
    {"name": "Priya", "marks": 95}
]

top_students = [
    student["name"]
    for student in students
    if student["marks"] >= 80
]

print("Top Students:", top_students)

print("\nProgram Completed Successfully!")