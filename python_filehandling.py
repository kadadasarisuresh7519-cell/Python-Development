# ==========================================
# FILE HANDLING & EXCEPTION HANDLING
# BASIC TO ADVANCED
# ==========================================

# ------------------------------------------
# 1. WRITE TO A FILE
# ------------------------------------------
print("----- WRITING TO FILE -----")

try:
    file = open("student.txt", "w")

    file.write("Name: Suresh\n")
    file.write("Course: Python\n")
    file.write("Age: 22\n")

    print("Data written successfully.")

    file.close()

except Exception as e:
    print("Error:", e)

# ------------------------------------------
# 2. READ FROM FILE
# ------------------------------------------
print("\n----- READING FILE -----")

try:
    file = open("student.txt", "r")

    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:
    print("File not found.")

# ------------------------------------------
# 3. APPEND DATA TO FILE
# ------------------------------------------
print("\n----- APPEND TO FILE -----")

try:
    file = open("student.txt", "a")

    file.write("College: ABC College\n")

    file.close()

    print("Data appended successfully.")

except Exception as e:
    print("Error:", e)

# ------------------------------------------
# 4. TRY EXCEPT EXAMPLE
# ------------------------------------------
print("\n----- TRY EXCEPT -----")

try:
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

# ------------------------------------------
# 5. TRY EXCEPT ELSE FINALLY
# ------------------------------------------
print("\n----- TRY EXCEPT ELSE FINALLY -----")

try:
    number = int(input("Enter a Number: "))

except ValueError:
    print("Invalid Input")

else:
    print("You entered:", number)

finally:
    print("Execution Completed")

# ------------------------------------------
# 6. MULTIPLE EXCEPT BLOCKS
# ------------------------------------------
print("\n----- MULTIPLE EXCEPT -----")

try:
    numbers = [10, 20, 30]

    index = int(input("Enter Index: "))

    print(numbers[index])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Please enter a valid integer.")

# ------------------------------------------
# 7. CUSTOM EXCEPTION
# ------------------------------------------
print("\n----- CUSTOM EXCEPTION -----")

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter Age: "))

    if age < 18:
        raise InvalidAgeError(
            "Age must be 18 or above."
        )

    print("Eligible")

except InvalidAgeError as e:
    print(e)

# ------------------------------------------
# 8. FILE READING LINE BY LINE
# ------------------------------------------
print("\n----- READ LINE BY LINE -----")

try:
    file = open("student.txt", "r")

    for line in file:
        print(line.strip())

    file.close()

except FileNotFoundError:
    print("File does not exist.")

# ------------------------------------------
# 9. USING WITH STATEMENT
# ------------------------------------------
print("\n----- WITH STATEMENT -----")

try:
    with open("sample.txt", "w") as file:
        file.write("Python File Handling Example")

    with open("sample.txt", "r") as file:
        print(file.read())

except Exception as e:
    print("Error:", e)

# ------------------------------------------
# 10. ADVANCED CUSTOM EXCEPTION
# ------------------------------------------
print("\n----- ADVANCED CUSTOM EXCEPTION -----")

class InvalidSalaryError(Exception):
    pass

def check_salary(salary):

    if salary < 10000:
        raise InvalidSalaryError(
            "Salary must be at least 10000"
        )

    return salary

try:
    salary = int(input("Enter Salary: "))

    print("Salary:", check_salary(salary))

except InvalidSalaryError as e:
    print(e)

# ------------------------------------------
# PROGRAM END
# ------------------------------------------
print("\nProgram Completed Successfully!")