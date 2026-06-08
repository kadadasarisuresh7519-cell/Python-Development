# ==========================================
# OBJECT ORIENTED PROGRAMMING (OOP)
# BASIC TO ADVANCED
# ==========================================

# ------------------------------------------
# 1. CLASS AND OBJECT
# ------------------------------------------

print("----- CLASS AND OBJECT -----")

class Student:
    def display(self):
        print("Welcome to Python OOP")

s1 = Student()
s1.display()

# ------------------------------------------
# 2. CONSTRUCTOR (__init__)
# ------------------------------------------

print("\n----- CONSTRUCTOR -----")

class Employee:

    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def show(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)

e1 = Employee(101, "Suresh")
e1.show()

# ------------------------------------------
# 3. ENCAPSULATION
# ------------------------------------------

print("\n----- ENCAPSULATION -----")

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance     # Private Variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)

print("Balance =", account.get_balance())

# ------------------------------------------
# 4. SINGLE INHERITANCE
# ------------------------------------------

print("\n----- SINGLE INHERITANCE -----")

class Person:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Teacher(Person):

    def subject(self):
        print("Subject: Python")

t1 = Teacher("Ravi")

t1.show_name()
t1.subject()

# ------------------------------------------
# 5. MULTILEVEL INHERITANCE
# ------------------------------------------

print("\n----- MULTILEVEL INHERITANCE -----")

class GrandParent:

    def grandparent_method(self):
        print("GrandParent Method")

class Parent(GrandParent):

    def parent_method(self):
        print("Parent Method")

class Child(Parent):

    def child_method(self):
        print("Child Method")

c1 = Child()

c1.grandparent_method()
c1.parent_method()
c1.child_method()

# ------------------------------------------
# 6. METHOD OVERRIDING
# ------------------------------------------

print("\n----- METHOD OVERRIDING -----")

class Animal:

    def sound(self):
        print("Animal Makes Sound")

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

d1 = Dog()

d1.sound()

# ------------------------------------------
# 7. POLYMORPHISM
# ------------------------------------------

print("\n----- POLYMORPHISM -----")

class Cat:

    def sound(self):
        print("Cat Meows")

class Cow:

    def sound(self):
        print("Cow Moos")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

# ------------------------------------------
# 8. USING SUPER()
# ------------------------------------------

print("\n----- SUPER FUNCTION -----")

class Vehicle:

    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car1 = Car("Toyota", "Innova")

car1.display()

# ------------------------------------------
# 9. ADVANCED EXAMPLE
# ------------------------------------------

print("\n----- ADVANCED EXAMPLE -----")

class Shape:

    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(10, 5)
circle = Circle(7)

print("Rectangle Area =", rectangle.area())
print("Circle Area =", circle.area())

# ------------------------------------------
# PROGRAM END
# ------------------------------------------

print("\nProgram Completed Successfully!")