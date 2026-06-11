students = {}

while True:
    print("\n=== STUDENT MANAGER ===")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Show All Students")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()
        age = input("Enter age: ").strip()
        city = input("Enter city: ").strip()
        student_class = int(input("Enter class: ").strip())

        students[name] = {
            "age": age,
            "city": city,
            "class": student_class
        }

        print("Student Added!")

    elif choice == "2":
        name = input("Search student: ").strip()

        if name in students:
            print(students[name])
        else:
            print("Student Not Found")

    elif choice == "3":
        if len(students) == 0:
            print("No Students Found")
        else:
            for name, details in students.items():
                print(name, ":", details)

    elif choice == "4":
        name = input("Enter student name: ").strip()

        if name in students:
            del students[name]
            print("Deleted Successfully")
        else:
            print("Student Not Found")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")