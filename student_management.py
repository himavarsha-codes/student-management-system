import json
import os

FILE_NAME = "students.json"


# Load students from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # OPTION 1 - ADD STUDENT
    if choice == "1":
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        branch = input("Enter branch: ")

        duplicate = False

        for student in students:
            if student["roll_number"] == roll_number:
                duplicate = True
                break

        if duplicate:
            print("A student with this roll number already exists!")
        else:
            student = {
                "name": name,
                "roll_number": roll_number,
                "branch": branch
            }

            students.append(student)
            save_students(students)

            print("Student added successfully!")

    # OPTION 2 - VIEW STUDENTS
    elif choice == "2":
        if len(students) == 0:
            print("No students found!")
        else:
            print("\n--- STUDENT LIST ---")

            for student in students:
                print("Name:", student["name"])
                print("Roll Number:", student["roll_number"])
                print("Branch:", student["branch"])
                print("-------------------")

    # OPTION 3 - SEARCH STUDENT
    elif choice == "3":
        roll_number = input("Enter roll number to search: ")

        found = False

        for student in students:
            if student["roll_number"] == roll_number:
                print("\nStudent found!")
                print("Name:", student["name"])
                print("Roll Number:", student["roll_number"])
                print("Branch:", student["branch"])
                found = True
                break

        if found == False:
            print("Student not found!")

    # OPTION 4 - UPDATE STUDENT
    elif choice == "4":
        roll_number = input("Enter roll number to update: ")

        found = False

        for student in students:
            if student["roll_number"] == roll_number:
                print("Student found!")

                student["name"] = input("Enter new name: ")
                student["branch"] = input("Enter new branch: ")

                save_students(students)

                print("Student details updated successfully!")
                found = True
                break

        if found == False:
            print("Student not found!")

    # OPTION 5 - DELETE STUDENT
    elif choice == "5":
        roll_number = input("Enter roll number to delete: ")

        found = False

        for student in students:
            if student["roll_number"] == roll_number:
                students.remove(student)
                save_students(students)

                print("Student deleted successfully!")
                found = True
                break

        if found == False:
            print("Student not found!")

    # OPTION 6 - EXIT
    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    # INVALID CHOICE
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")