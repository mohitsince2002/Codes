import random

students = []

while True:
    print('\nStudent Management System')
    print('1. Add Student')
    print('2. View All Students')
    print('3. Search Student')
    print('4. Update Student')
    print('5. Delete Student')
    print('6. Exit')

    choice = input('Enter your choice (1-6): ')

    if choice == '1':
        student_id = random.randint(100, 999)
        student_name = input('Enter student name: ')
        student_age = input('Enter student age: ')
        student_city = input('Enter student city: ')

        new_student = {
            'id': student_id,
            'name': student_name,
            'age': student_age,
            'city': student_city
        }

        students.append(new_student)
        print('Student Added Successfully!')
        print(f'Kindly note your Student ID: {student_id}')

    elif choice == '2':
        if not students:
            print('No Records Found')
        else:
            print('Students List:')
            for student in students:
                print('===================================')
                print(f"Student ID   : {student['id']}")
                print(f"Student Name : {student['name']}")
                print(f"Student Age  : {student['age']}")
                print(f"Student City : {student['city']}")
                print('===================================')

    elif choice == '3':
        try:
            student_id = int(input('Enter Student ID to search: '))
        except ValueError:
            print("Invalid ID. Must be a number.")
            continue

        found = False
        for student in students:
            if student['id'] == student_id:
                print('===================================')
                print(f"Student ID   : {student['id']}")
                print(f"Student Name : {student['name']}")
                print(f"Student Age  : {student['age']}")
                print(f"Student City : {student['city']}")
                print('===================================')
                found = True
                break
        if not found:
            print('Student Not Found')

    elif choice == '4':
        found = False
        student_id = int(input("Enter Student Id - "))
        for student in students:
            if student["id"] == student_id:
                print(f"Current Details {student}")

                student_name = input("Enter student Name(Press Enter to skip) -")
                student_name = input("Enter student Age(Press Enter to skip) -")
                student_name = input("Enter student City(Press Enter to skip) -")
                
                if student_name:
                    student["name"] = student_name
                if student_city:
                    student["city"] = student_city
                if student_age:
                    student["age"] = student_age
                    
                print("Student Updates Successfully")


    elif choice == '5':
        found = False
        student_id = input('Enter Student Id to delete - ')
        for student in students : 
            if student["id"] == student_id:
                students.remove(student)
                print("Student Deleted")
                found = True
                break
        if not found:
            print('Student Not Found! ')
            
            
    elif choice == '6':
        print('Exiting Student Management System. Goodbye!')
        break

    else:
        print('Invalid choice! Please try again.')
        
        