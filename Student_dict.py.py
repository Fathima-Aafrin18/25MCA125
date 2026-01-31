students = {}

while True:
    print("\n===== Student Marks Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Subject Mark")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add Student
    if choice == 1:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")

        marks = {}
        n = int(input("Enter number of subjects: "))

        for i in range(n):
            subject = input(f"Enter subject {i+1} name: ")
            mark = float(input(f"Enter Mark for {subject}: "))
            marks[subject] = mark

        students[roll] = {
            "name": name,
            "marks": marks
        }
        print("Student added successfully!")

    # 2. View All Students
    elif choice == 2:
        if not students:
            print("No student records found.")
        else:
            for roll, details in students.items():
                total = sum(details["marks"].values())
                percentage = total / len(details["marks"])

                print("\nRoll Number:", roll)
                print("Name:", details["name"])
                print("Marks:")
                for subject, mark in details["marks"].items():
                    print(f"  {subject} : {mark}")
                print("Total Marks:", total)
                print("Percentage:", round(percentage, 2), "%")

    # 3. Search Student
    elif choice == 3:
        roll = int(input("Enter Roll Number to search: "))
        if roll in students:
            details = students[roll]
            total = sum(details["marks"].values())
            percentage = total / len(details["marks"])

            print("Name:", details["name"])
            print("Marks:")
            for subject, mark in details["marks"].items():
                print(f"  {subject} : {mark}")
            print("Total Marks:", total)
            print("Percentage:", round(percentage, 2), "%")
        else:
            print("Student not found.")

    # 4. Update Subject Mark
    elif choice == 4:
        roll = int(input("Enter Roll Number: "))
        if roll in students:
            subject = input("Enter subject name to update: ")
            if subject in students[roll]["marks"]:
                new_mark = float(input(f"Enter new mark for {subject}: "))
                students[roll]["marks"][subject] = new_mark
                print("Mark updated successfully!")
            else:
                print("Subject not found.")
        else:
            print("Student not found.")

    # 5. Delete Student
    elif choice == 5:
        roll = int(input("Enter Roll Number to delete: "))
        if roll in students:
            del students[roll]
            print("Student record deleted.")
        else:
            print("Student not found.")

    # 6. Exit
    elif choice == 6:
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
