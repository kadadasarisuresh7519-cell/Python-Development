import json

class Student:

    def __init__(self, sid, name, age, course, marks):
        self.sid = sid
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            "ID": self.sid,
            "Name": self.name,
            "Age": self.age,
            "Course": self.course,
            "Marks": self.marks
        }


class StudentManagementSystem:

    def __init__(self):
        self.students = []
        self.load_data()

    # Add Student
    def add_student(self):

        try:
            sid = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            student = Student(
                sid,
                name,
                age,
                course,
                marks
            )

            self.students.append(student)

            print("\nStudent Added Successfully!")

        except ValueError:
            print("Invalid Input!")

    # View Students
    def view_students(self):

        if not self.students:
            print("\nNo Records Found!")
            return

        print("\n------ STUDENT RECORDS ------")

        for student in self.students:

            print(
                f"ID: {student.sid} | "
                f"Name: {student.name} | "
                f"Age: {student.age} | "
                f"Course: {student.course} | "
                f"Marks: {student.marks}"
            )

    # Search Student
    def search_student(self):

        sid = int(input("Enter Student ID: "))

        for student in self.students:

            if student.sid == sid:

                print("\nStudent Found")
                print("ID:", student.sid)
                print("Name:", student.name)
                print("Age:", student.age)
                print("Course:", student.course)
                print("Marks:", student.marks)

                return

        print("Student Not Found!")

    # Update Student
    def update_student(self):

        sid = int(input("Enter Student ID: "))

        for student in self.students:

            if student.sid == sid:

                student.name = input("New Name: ")
                student.age = int(input("New Age: "))
                student.course = input("New Course: ")
                student.marks = float(
                    input("New Marks: ")
                )

                print("Student Updated!")
                return

        print("Student Not Found!")

    # Delete Student
    def delete_student(self):

        sid = int(input("Enter Student ID: "))

        for student in self.students:

            if student.sid == sid:

                self.students.remove(student)

                print("Student Deleted!")
                return

        print("Student Not Found!")

    # Statistics
    def statistics(self):

        if not self.students:
            print("No Data Available!")
            return

        marks = [
            student.marks
            for student in self.students
        ]

        print("\n------ REPORT ------")
        print("Total Students:", len(marks))
        print("Highest Marks:", max(marks))
        print("Lowest Marks:", min(marks))
        print("Average Marks:",
              round(sum(marks) / len(marks), 2))

    # Save Data
    def save_data(self):

        data = [
            student.to_dict()
            for student in self.students
        ]

        with open(
            "students.json",
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # Load Data
    def load_data(self):

        try:

            with open(
                "students.json",
                "r"
            ) as file:

                data = json.load(file)

                for item in data:

                    student = Student(
                        item["ID"],
                        item["Name"],
                        item["Age"],
                        item["Course"],
                        item["Marks"]
                    )

                    self.students.append(student)

        except FileNotFoundError:
            pass

    # Menu
    def menu(self):

        while True:

            print("\n")
            print("===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Statistics")
            print("7. Save & Exit")

            choice = input(
                "Enter Choice: "
            )

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.statistics()

            elif choice == "7":

                self.save_data()

                print(
                    "Data Saved Successfully!"
                )

                print(
                    "Thank You!"
                )

                break

            else:
                print(
                    "Invalid Choice!"
                )


# Main Program
sms = StudentManagementSystem()
sms.menu()