# -------------------------------
# List Operations
# -------------------------------
fruits = ["Apple", "Banana", "Mango"]

# Add an element
fruits.append("Orange")

# Remove an element
fruits.remove("Banana")

print("List Operations:")
print("Fruits List:", fruits)

# -------------------------------
# Tuple Handling
# -------------------------------
student = ("Suresh", 22, "Python")

print("\nTuple Handling:")
print("Student Name:", student[0])
print("Student Age:", student[1])
print("Course:", student[2])

# -------------------------------
# Dictionary Usage
# -------------------------------
employee = {
    "id": 101,
    "name": "Suresh",
    "salary": 50000
}

print("\nDictionary Usage:")
print("Employee Details:", employee)
print("Employee Name:", employee["name"])

# Add a new key-value pair
employee["department"] = "IT"
print("Updated Dictionary:", employee)

# -------------------------------
# Set Operations
# -------------------------------
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet Operations:")
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# -------------------------------
# List Comprehension
# -------------------------------
numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print("\nList Comprehension:")
print("Original Numbers:", numbers)
print("Squares:", squares)